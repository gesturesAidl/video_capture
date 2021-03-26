

# VIDEO TO msg

########################################################################
# Mock class Bytes

import numpy as np
import cv2

self.last_clip = None
self.frameSize = (170,100)
self.fps = 12
self.video_writer = cv2.VideoWriter_fourcc(*'mp4v')
self.dtype = dtype('uint8')
self.out = '' #Folder path

def get_video(msg):
    
    current_clip = [np.frombuffer(frame, dtype=self.dtype).reshape(100,170,3) for frame in msg['data']]
    
    if self.last_clip:
        video = self.last_clip + current_clip
        video_out=cv2.VideoWriter(self.out+str(msg['init'])+'.mp4', self.video_writer,self.fps,self.frameSize)
        
        for frame in video:
            video_out.write(frame)
        video_out.release()
    
    self.last_clip = current_clip  



# REQUEST
import cv2
import time



device_index = 0
fps = 12
frameSize = (170, 100)
video_lenght = 36//2  
video_cap = cv2.VideoCapture(device_index)

k = 0
msg = {
    'init':time.time(),
    'end':None,
    'data':[]
}

for i in range(video_length):

    ret, video_frame = video_cap.read()
    time.sleep(0.05)
    msg['data'].append(cv2.resize(video_frame,frameSize).tobytes())
    
msg['end'] = time.time()
video_cap.release()




# LOOP (MES FORMES)

import cv2
import time



device_index = 0
fps = 12
frameSize = (170, 100)
video_lenght = 36  
video_cap = cv2.VideoCapture(device_index)

k = 0
msg = {
    'init':time.time(),
    'end':None,
    'data':[]
}

while True:

    ret, video_frame = video_cap.read()
    k += 1
    time.sleep(0.05)
    msg['data'].append(cv2.resize(video_frame,frameSize).tobytes())
    
    if k==video_lenght//2:
        msg['end'] = time.time()
        # FUNCTION HERE TO SEND THE DICT
        send('ToTheMoon')
        msg = {
        'init':time.time(),
        'end':None,
        'data':[]
        }
        k = 0

video_cap.release()
