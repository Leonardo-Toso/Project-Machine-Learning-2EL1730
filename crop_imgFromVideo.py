import cv2
import numpy as np
import os
import glob



img = glob.glob('*.jpg')
for img_path in img:
	img = cv2.imread(img_path)
	img_crop = img[:1010,810:1320]
	cv2.imwrite (img_path,img_crop)

