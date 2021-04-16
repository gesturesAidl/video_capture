import subprocess
import os
from pathlib import Path


class GUIController:

    def __init__(self):
        self.current_dir = str(Path.home()) + "/AIDL"
        self.file_count = 0
        self.dir_count = 0
        if not os.path.exists(self.current_dir):
            subprocess.call(["mkdir", self.current_dir])
        self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir])
        self.files_process_pid = None
        self.popup_pid = None
        self.last_clip_was_gesture = False

    # Create new file with template name "file_{file_count}.txt"
    def create_file(self):
        self.last_clip_was_gesture = True
        if self.files_process_pid is not None:
            self.show_info_msg("Unable to create a file when there is already one opened.")
        else:
            self.file_count = self.file_count+1
            file_name = "file_" + str(self.file_count) + '.txt'
            subprocess.call(["touch", self.current_dir + "/ " + file_name])
            self.files_process_pid = subprocess.Popen(["gedit", self.current_dir + "/ " + file_name])

    # Close opened file window
    def close_file(self):
        self.last_clip_was_gesture = True
        if self.files_process_pid is None:
            self.show_info_msg("Unable to close a file because there is no file opened")
        else:
            subprocess.call(["kill", "-9", str(self.files_process_pid.pid)])
            self.files_process_pid = None
            self.refresh_view()

    # Create new directory in current directory with template name "dir_{dir_count}"
    def create_dir(self):
        self.last_clip_was_gesture = True
        self.current_dir = self.current_dir + '/dir_' + str(self.dir_count)
        subprocess.call(["mkdir", self.current_dir])
        subprocess.call(["kill", "-9", str(self.dir_process_pid.pid)])
        self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir])

    # Remove all files & directories of current directory
    def rm_all_in_dir(self):
        self.last_clip_was_gesture = True
        list_elems = os.listdir(self.current_dir)
        for elem in list_elems:
            subprocess.call(["rm", "-rf", self.current_dir + "/" + elem])
        self.refresh_view()

    # Move one directory back in files
    def move_back_in_dirs(self):
        self.last_clip_was_gesture = True
        parts = self.current_dir.split("/")
        last = parts[len(parts) - 1]
        if self.current_dir.replace('/'+last, '') == str(Path.home()):
            self.show_info_msg("You are in the root dir of this app. You cannot move back any other step.")
        else:
            subprocess.call(["kill", "-9", str(self.dir_process_pid.pid)])
            self.current_dir = self.current_dir.replace('/'+last, '')
            self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir])

    # Move one directory forward in files
    def move_fw_in_dirs(self):
        self.last_clip_was_gesture = True
        for elem in os.listdir(self.current_dir):
            if os.path.isdir(self.current_dir + "/" + elem):
                subprocess.call(["kill", "-9", str(self.dir_process_pid.pid)])
                self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir  + "/" + elem])
                return
        self.show_info_msg("no dir exists in order to move into it.")

    # Close info popup opened to inform of app error
    def close_info_popup(self):
        self.last_clip_was_gesture = True
        if self.popup_pid is not None:
            subprocess.call(["kill", "-9", str(self.popup_pid.pid)])
        self.popup_pid = None

    # Open info window with message in @{msg}
    def show_info_msg(self, msg):
        if self.popup_pid is not None:
            self.close_info_popup()
        self.popup_pid = subprocess.Popen(["zenity", "--info", '--text="' + msg + '"', "&"])

    def refresh_view(self):
        subprocess.call(["kill", "-9", str(self.dir_process_pid.pid)])
        self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir])

    def last_was_no_gesture(self):
        self.last_clip_was_gesture = False

    def was_last_gesture(self):
        return self.last_clip_was_gesture

