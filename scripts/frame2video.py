import cv2
import numpy as np
import glob
import os
import time
#from progress.bar import IncrementalBar
import logging


folderIn = "/mnt/disks/jester_dataset/dataset/20bn-jester-v1/"
folderOut = "/home/gestures_aidl/videos/"

if not os.path.exists(folderOut):
    os.makedirs(folderOut)

directories = [f for f in  os.scandir(folderIn) if f.is_dir() ]
#bar = IncrementalBar('Completed', max = len(directories),  suffix='%(index)d/%(max)d - %(percent).1f%% - ETA: %(eta)ds ')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

logging.basicConfig(filename='/home/gestures_aidl/scripts/logs/frame2video.log')
log_int = 50
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
vid_s_time = time.time()

for num, directory in enumerate(directories):
    #print("Processing images from " + directory.name)
    img_array = []
    if os.path.exists(folderOut + directory.name+'.mp4'):
        continue
    for filename in sorted(glob.glob(directory.path+'/*.jpg')):
        img = cv2.imread(filename)
        img_array.append(img)

    height, width, layers = img.shape
    size = (width,height)
    out = cv2.VideoWriter(folderOut + directory.name+'.mp4', fourcc, 12.0, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    if num > 0 and num % log_int == 0:
        vid_e_time = time.time()
        loop_t = vid_e_time - vid_s_time
        vid_s_time = time.time()
        t = (len(directories) - num)/log_int * loop_t /3600
        logger.info('%04d/%04d is done (%4.2f%%). Time for processing %02d videos: %4.2f seconds. ETA: %4.2fh' % (num, len(directories),num/len(directories)*100,log_int, loop_t, t))
        



    #time.sleep(0.2)
    #bar.next()
#bar.finish()
