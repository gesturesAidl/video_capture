import cv2
import time
import json
import logging
from datetime import datetime


class VideoRecorder:

    # Video class based on openCV
    def __init__(self, rabbit_template):
        self.rabbit_template = rabbit_template
        self.fps = 12
        self.frameSize = (170, 100)
        self.video_lenght = 36
        self.video_cap = cv2.VideoCapture(0)

    # Videos starts being recorded
    def record(self):
        k = 0
        data = []
        while True:

            ret, video_frame = self.video_cap.read()
            k += 1
            time.sleep(0.05)
            data.append(cv2.resize(video_frame, self.frameSize))

            if k == self.video_lenght // 2:

                # Publish video
                json_string = json.dumps([ob.tolist() for ob in data])
                logging.info("Video sent at: " + str(datetime.now()))
                self.rabbit_template.publish_video(json_string)
                k = 0
                data = []

    def stop(self):
        self.video_cap.release()
