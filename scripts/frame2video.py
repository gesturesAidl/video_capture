import cv2
import numpy as np
import glob
import os
import time
from progress.bar import IncrementalBar

folderIn = "/mnt/disks/disk-1/jester_dataset/dataset/20bn-jester-v1/"
folderOut = "/home/gestures_aidl/aidl/videos/"

if not os.path.exists(folderOut):
    os.makedirs(folderOut)

directories = [f for f in  os.scandir(folderIn) if f.is_dir() ]
bar = IncrementalBar('Completed', max = len(directories),  suffix='%(index)d/%(max)d - %(percent).1f%% - ETA: %(eta)ds ')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

for directory in directories:
    #print("Processing images from " + directory.name)
    img_array = []
    for filename in glob.glob(directory.path+'/*.jpg'):
        img = cv2.imread(filename)
        img_array.append(img)

    height, width, layers = img.shape
    size = (width,height)
    out = cv2.VideoWriter(folderOut + directory.name+'.mp4', fourcc, 12.0, size)
    
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    #time.sleep(0.2)
    bar.next()
bar.finish()
