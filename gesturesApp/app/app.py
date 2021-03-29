import time
import os
from pathlib import Path
import sys

workdir = '{abs_path_to_your_project}' + '/aidl_gesture_recognition'
sys.path.insert(0, workdir)

from gesturesApp.app.video_recorder.videorecorder import VideoRecorder
from gesturesApp.app.config.RabbitTemplate import RabbitTemplate

from dotenv import load_dotenv


def load_env():
    env_path = Path(workdir + '/gesturesApp/env') / '.env'
    load_dotenv(dotenv_path=env_path)


if __name__ == '__main__':
    # Load environment vars
    load_env()

    rabbit_template = RabbitTemplate()
    video_manager = VideoRecorder(rabbit_template)
    video_manager.record()

