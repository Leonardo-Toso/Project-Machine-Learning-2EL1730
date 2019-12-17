import cv2
import numpy as np
import os
import glob

def paint(img_path,x1,y1,x2,y2,x3,y3,x4,y4):
	img = cv2.imread(img_path)
	linhas,colunas,layer = img.shape
	dx = colunas/970
	dy = linhas/1790
	x1*=dx
	x2*=dx
	x3*=dx
	x4*=dx
	y1*=dy
	y2*=dy
	y3*=dy
	y4*=dy
	
	print(colunas ,linhas)
	
	a = (y1-y2)/(x1-x2)
	b = y1 - a*x1
	#right
	a2 = (y3-y4)/(x3-x4)
	b2 = y3 - a2*x3
	img = np.array(img)
	
	for y in range ((linhas)): #colunas
		
		posX = int((y-b) / a)
		posX2 = int((y - b2)/a2)
	
		img[y, :posX] = [0, 0, 0]	
		img[y,posX2:] = [0, 0, 0]
	
	cv2.imwrite (img_path[:-4] + "teste.png",img)
	

	



