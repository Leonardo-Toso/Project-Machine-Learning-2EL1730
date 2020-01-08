import cv2
import numpy as np
import os
import glob
from paintAfterCrop import paint


img = glob.glob('DSCN1650.JPG')
#img = glob.glob('*.JPG')

for img_path in img:
	paint(img_path,46,1703,391,167,591,140,917,1563)#(x(number of collumns),y(number of lines))bottom left corner, top left corner, top right corner, bottom right corner
	

