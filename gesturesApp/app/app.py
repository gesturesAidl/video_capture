import time
import os
from pathlib import Path
import logging
import sys

workdir = os.getcwd()
sys.path.insert(0, workdir)

from gesturesApp.app.controller.gui_controller import GUIController
from gesturesApp.app.video_recorder.videorecorder import VideoRecorder
from gesturesApp.app.config.RabbitTemplate import RabbitTemplate

from dotenv import load_dotenv


def load_env():
    env_path = Path(workdir + '/gesturesApp/env') / '.env'
    load_dotenv(dotenv_path=env_path)


if __name__ == '__main__':

    logging.getLogger().setLevel(logging.INFO)

    # Load environment vars
    load_env()

    gui_controller = GUIController()
    rabbit_template = RabbitTemplate(gui_controller)
    video_manager = VideoRecorder(rabbit_template)
    logging.info("[X] Start recording: ")
    video_manager.record()
