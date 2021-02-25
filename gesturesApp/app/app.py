import time
import os
from pathlib import Path

from video_recorder.videorecorder import VideoRecorder
from dotenv import load_dotenv


def load_env():
    env_path = Path('env') / '.env'
    load_dotenv(dotenv_path=env_path)


if __name__ == '__main__':
    # Load environment vars
    load_env()

    # Start recording
    recorder = VideoRecorder()
    recorder.record()
    time.sleep(3)
    recorder.stop()
