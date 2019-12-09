import cv2
import numpy as np
import os
import glob
from paint import paint


img = glob.glob('*.JPG')
for img_path in img:
	paint(img_path,1770,2290,3330,1930,3250,2830,2000,2550)
	
'''
...x1..x2..........> xmax = num_colunas
.       
.       
y2     o
.   
.   
y1 o
.
.
.
ymax = num_linhas

'''
#cv2.imshow('output', img)
#cv2.waitKey()
'''
print(img.shape)

h = int( img.shape[1]*0.222 )
w = int( img.shape[0]*0.222 )
newImg = cv2.resize(img,(h,w))
resize
print(newImg.shape)
cv2.imwrite('ru1.jpg',newImg)

#newImg = (newImg-127.5)/128
newImg = (newImg-127.5)/128

local = os.getcwd()

a = [name for name in os.listdir(local) if name.endswith('.jpg')]
glob.glob('*.jpg')
'''

