import cv2
import time
import json
import logging
from datetime import datetime

logger = logging.getLogger('logger')

class VideoRecorder:

    # Video class based on openCV
    def __init__(self, rabbit_template):
        self.rabbit_template = rabbit_template
        self.fps = 12
        self.frameSize = (170, 100)
        self.video_lenght = 36
        self.video_cap = cv2.VideoCapture(0)
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    # Videos starts being recorded
    def record(self):
        k = 0
        data = []
        resp = ''
        count = 0

        ########## Uncomment all comments from here on for green/red circle #######
        
        # radius = 30
        # center_coordinates = (30, 30)
        # color = [(0, 255, 0),(0, 0, 255)] # red-green
        # red = (0, 0, 255)
        # green = (0, 255, 0)
        # thickness = -1

        while True:
            ret, video_frame = self.video_cap.read()
            k += 1
            time.sleep(0.05)
            data.append(cv2.resize(video_frame, self.frameSize))
            tempResp = self.rabbit_template.get_response()
            if tempResp != None:
                x = json.loads(json.loads(tempResp))
                cv2.putText(video_frame, str(x["label"]), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255),2)
            
            # video_frame = cv2.circle(video_frame, center_coordinates, radius, color[count], thickness)
            
            cv2.imshow('Gestures App', video_frame)
            cv2.waitKey(1)
            if k == self.video_lenght // 2:
                count = (count + 1) % 2
                
                # video_frame = cv2.circle(video_frame, center_coordinates, radius, red, thickness)
                # cv2.imshow('Gestures App', video_frame)
                # cv2.waitKey(1)

                json_string = json.dumps([ob.tolist() for ob in data])
                logger.info("Video sent at: " + str(datetime.now()))
                self.rabbit_template.publish_video(json_string)
                k = 0
                data = []
                
                # video_frame = cv2.circle(video_frame, center_coordinates, radius, color[count], thickness)
                # cv2.imshow('Gestures App', video_frame)
                # cv2.waitKey(1)

    def stop(self):
        self.video_cap.release()
