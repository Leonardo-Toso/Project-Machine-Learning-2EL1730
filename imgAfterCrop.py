import cv2
import numpy as np
import os
import glob
from paintAfterCrop import paint


img = glob.glob('DSCN1650.JPG')

for img_path in img:
	paint(img_path,46,1703,391,167,591,140,917,1563)
	

