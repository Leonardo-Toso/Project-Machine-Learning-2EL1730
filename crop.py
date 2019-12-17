import cv2
import numpy as np
import os
import glob



img = glob.glob('*.JPG')
for img_path in img:
	img = cv2.imread(img_path)
	img_crop = img[1650:3440,1900:2870]
	cv2.imwrite (img_path,img_crop)

