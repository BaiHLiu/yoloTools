from utils.plots import plot_one_box
import cv2
import numpy as np
import json
import os

'''
Batch plot images with your annotations, for valid.

Usage:
    0.This file should be put in the yolov5-5.0 src directory.
    1.Organize your files, contains 'images' and 'labels'.
    2.Set your root path.
    3.python3 validPlot.py
'''

# Root path
dataPath = './data/dam/'

fileList = os.listdir(dataPath+'images')

def plot(imgFile, labFile):
    img0 = cv2.imread(imgFile)
    labels = None
    with open(labFile) as f:
        labels = json.load(f)['outputs']['object']
    
    for lab in labels:
        xyxyDict = lab['bndbox']
        xyxyList = list(xyxyDict.values())
        
        img0 = plot_one_box(xyxyList, img0, label=lab['name'])

    cv2.imwrite(imgFile, img0)
     

if __name__ == "__main__":
    idx = 0
    for fileName in fileList:
        idx += 1
        amount = len(fileList)
        
        try:
            plot(dataPath+'images/'+fileName, dataPath+'labels/'+fileName.split('.')[0]+'.json')
        except:
            print(f'[!] idx/{amount} Failed!')
        else:
            pass
    
    print('Well done.')

