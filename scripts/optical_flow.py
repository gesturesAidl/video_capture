import cv2
import numpy as np
import time
import logging
import os

# Output floder. If not exists, create
folderOut = "/home/gestures_aidl/optical_flow/"
if not os.path.exists(folderOut):
    os.makedirs(folderOut)

# Get video list information - videos.txt = file containing full path for each video to process, one per line.
video_list = "/home/gestures_aidl/scripts/txt/videos.txt"
f = open(video_list, 'r')
video_list = f.readlines()

# Init logging
logging.basicConfig(filename='./logs/optical_flow.log')
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
log_int = 50
vid_s_time = time.time()

for vid, vline in enumerate(video_list):
        
    video_path = vline.split()[0]
    video_name = video_path.split('/')[-1]

    if os.path.exists(folderOut + "opfw_" + video_name):
        continue
    
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(frame1)
    hsv[...,1] = 255

    array = []

    for i in range(length-1):
        ret, frame2 = cap.read()
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

        flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
        hsv[...,0] = ang*180/np.pi/2
        hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
        rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
        
        array.append(rgb)
        prvs = next

    cap.release()
    cv2.destroyAllWindows()

    height, width, layers = rgb.shape
    size = (width,height)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(folderOut + "opfw_" + video_name, fourcc, 12.0, size)
        
    for i in range(len(array)):
        out.write(array[i])
    out.release()

    if vid > 0 and vid % log_int == 0:
        vid_e_time = time.time()
        loop_t = vid_e_time - vid_s_time
        t = (len(video_list) - vid)/log_int * loop_t /3600
        logger.info('%04d/%04d is done (%4.2f%%). Time for extracting optical flow %02d videos: %4.2f seconds. ETA: %4.2fh' % (vid, len(video_list),vid/len(video_list)*100, log_int, loop_t, t))
        vid_s_time = time.time()
