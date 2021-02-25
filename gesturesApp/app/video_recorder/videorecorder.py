import cv2
import wave
import threading
import time
import os


class VideoRecorder:

    # Video class based on openCV
    def __init__(self):

        self.open = True
        self.device_index = 0
        self.fps = 6  # fps should be the minimum constant rate at which the camera can
        self.fourcc = "MJPG"  # capture images (with no decrease in speed over time; testing is required)
        self.frameSize = (640, 480)  # video formats and sizes also depend and vary according to the camera used
        self.video_path_to_file = os.environ.get('VIDEO_OUTPUT', './output_videos') + os.environ.get('VIDEO_FILENAME')
        self.video_cap = cv2.VideoCapture(self.device_index)
        self.video_writer = cv2.VideoWriter_fourcc(*self.fourcc)
        self.video_out = cv2.VideoWriter(self.video_path_to_file, self.video_writer, self.fps, self.frameSize)
        self.frame_counts = 1
        self.start_time = time.time()

    # Video starts being recorded
    def record(self):
        # counter = 1
        timer_start = time.time()
        timer_current = 0

        while self.open:
            ret, video_frame = self.video_cap.read()
            if ret:

                self.video_out.write(video_frame)
                # print str(counter) + " " + str(self.frame_counts) + " frames written " + str(timer_current)
                self.frame_counts += 1
                # counter += 1
                # timer_current = time.time() - timer_start
                time.sleep(0.16)
                # gray = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
                # cv2.imshow('video_frame', gray)
                # cv2.waitKey(1)
            else:
                break
                # 0.16 delay -> 6 fps

    # Finishes the video recording therefore the thread too
    def stop(self):
        if self.open:
            self.open = False
            self.video_out.release()
            self.video_cap.release()
            cv2.destroyAllWindows()
        else:
            pass

    # Launches the video recording function using a thread
    def start(self):
        video_thread = threading.Thread(target=self.record)
        video_thread.start()
