import subprocess
import os
from pathlib import Path


class GUIController:

    def __init__(self):
        self.current_dir = str(Path.home()) + "/AIDL"
        self.file_count = 0
        self.dir_count = 0
        subprocess.call(["mkdir", self.current_dir])
        self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir])
        self.files_process_pid = None
        self.popup_pid = None

    # Create new file with template name "file_{file_count}.txt"
    def create_file(self):
        self.file_count = self.file_count+1
        file_name = "file_" + str(self.file_count) + '.txt'
        subprocess.call(["touch", self.current_dir + "/ " + file_name])
        self.files_process_pid = subprocess.Popen(["gedit", self.current_dir + "/ " + file_name])

    # Close opened file window
    def close_file(self):
        if self.files_process_pid is None:
            self.show_info_msg("Unable to close a file because there is no file opened")
        else:
            subprocess.call(["kill", "-9", str(self.files_process_pid.pid)])

    # Create new directory in current directory with template name "dir_{dir_count}"
    def create_dir(self):
        self.current_dir = self.current_dir + '/dir_' + str(self.dir_count)
        subprocess.call(["mkdir", self.current_dir])
        subprocess.call(["kill", "-9", str(self.dir_process_pid.pid)])
        self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir])

    # Remove all files & directories of current directory
    def rm_all_in_dir(self):
        list_elems = os.listdir(self.current_dir)
        for elem in list_elems:
            subprocess.call(["rm", "-rf", self.current_dir + "/" + elem])

    # Move one directory back in files
    def move_back_in_dirs(self):
        parts = self.current_dir.split("/")
        last = parts[len(parts) - 1]
        if self.current_dir.replace('/'+last, '') == str(Path.home()):
            pass
        else:
            self.current_dir = self.current_dir.replace('/'+last, '')
            subprocess.call(["kill", "-9", str(self.dir_process_pid.pid)])
            self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir])

    # Move one directory forward in files
    def move_fw_in_dirs(self):
        for elem in os.listdir(self.current_dir):
            if os.path.isdir(self.current_dir + "/" + elem):
                subprocess.call(["kill", "-9", str(self.dir_process_pid.pid)])
                self.dir_process_pid = subprocess.Popen(["nautilus", self.current_dir  + "/" + elem])
                return
        self.show_info_msg("no dir exists in order to move into it")

    # Close info popup opened to inform of app error
    def close_info_popup(self):
        subprocess.call(["kill", "-9", str(self.popup_pid.pid)])
        self.popup_pid = None

    # Open info window with message in @{msg}
    def show_info_msg(self, msg):
        if self.popup_pid is not None:
            self.close_info_popup()
        self.popup_pid = subprocess.Popen(["zenity", "--info", '--text="' + msg + '"', "&"])

