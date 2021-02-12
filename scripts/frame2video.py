import cv2
import numpy as np
import glob
import os
import time
import logging

folderIn = "/mnt/disks/disk-1/jester_dataset/dataset/20bn-jester-v1/"
folderOut = "/home/gestures_aidl/aidl/videos/"

logger = logging.getLogger('logger')

if not os.path.exists(folderOut):
    os.makedirs(folderOut)
img_array = []
directories = [f for f in  os.scandir(folderIn) if f.is_dir() ]
sx = len(directories)/1000
index = 0
start_time = time.time()
for directory in directories:
    #print("Processing images from " + directory.name)
    for filename in glob.glob(directory.path+'/*.jpg'):
        #print("Image: " +filename)
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(folderOut + directory.name+'.mp4', fourcc, 12.0, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    if index % 20 == 0:
        end_time = time.time()
        logger.info('Time running: %4.2f minutes' % ((end_time - start_time) / 60))
        print('Time running: '+ "{:.2f}".format((end_time - start_time) / 60) + ' minutes')
        print('Completed ' + "{:.2f}".format((index/sx)) + '% of the datbase')
    index +=1
    print(index)

end_time = time.time()
logger.info('Total time for video conversion is  %4.2f minutes' % ((end_time - start_time) / 60))



 

