'''
Description: An image compress and orgnization tools for yolo.
Author: Catop
Date: 2022-01-27 22:47:28
LastEditTime: 2022-01-28 10:04:25
'''

import os
import shutil
import cv2
import random

'''
Batch compress images, and organize them into Yolo directory format.
Input directory:
    .
    ├── classes.txt
    ├── images/
    └── labels/
Output directory:
    .
    ├── classes.txt
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── valid/
    │   ├── images/
    │   └── labels/
    └── test/
        ├── images/
        └── labels/
Usage:
    1.Organize your files into input directory pattern.
    2.Modify your root path.
    3.Set dataset ratio of train, valid, test.


'''

#########################################
# Root path
path = "./"

# Dataset ratio
dataset = {
    'train':0.4,
    'valid':0.4,
    'test':0.2
}
#########################################

# Randomly sort the different datasets.
fileList = os.listdir(path+'images')
random.shuffle(fileList)

# Create output directory
for ds in dataset.keys():
    if not os.path.exists(path+ds):
        os.makedirs(path+ds)
        os.makedirs(path+ds+'/images')
        os.makedirs(path+ds+'/labels')

# Images compress
class Compress_img:
    
    def __init__(self, img_path):
        self.img_path = img_path
        self.img_name = img_path.split('/')[-1]

    def compress_img_CV(self, compress_rate=0.5, show=False):
        img = cv2.imread(self.img_path)
        heigh, width = img.shape[:2]
        img_resize = cv2.resize(img, (int(width*compress_rate), int(heigh*compress_rate)),
                                interpolation=cv2.INTER_AREA)
        cv2.imwrite(self.img_path, img_resize)

        return compress_rate

# Organize files
def org(f, dst):
    imgFile = path+'images/'+f
    txtFile = path+'labels/'+f.split('.')[0]+'.txt'

    shutil.move(imgFile, path+dst+'/images')
    shutil.move(txtFile, path+dst+'/labels')


if __name__ == '__main__':
    
    idx = 0
    num = len(fileList)

    typeCont = {}
    for t in dataset.keys():
        typeCont[t] = 0

    for f in fileList:
        idx += 1
        try:
            img_path = path+'images/'+f
            compress = Compress_img(img_path)
            compressRate = compress.compress_img_CV()

            for t in typeCont.keys():
                
                if(typeCont[t] < num*dataset[t]):
                    org(f, t)
                    typeCont[t] += 1
                    break
        except:
            print(f"[!] {idx}/{num} Faild : {f}")
        else:
            print(f"[+] {idx}/{num} Success : {f}")
    

    os.removedirs(path+'images')
    os.removedirs(path+'labels')