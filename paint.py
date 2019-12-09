import cv2
import numpy as np
import os
import glob

def paint(img_path,x1,y1,x2,y2,x3,y3,x4,y4):
	img = cv2.imread(img_path,0)
	colunas,linhas = img.shape
	img=cv2.rectangle(img,(0,0),(int(colunas),int(linhas*0.35)),(0,0,0),-1)
	#left
	a = (y1-y2)/(x1-x2)
	b = y1 - a*x1
	#right
	a2 = (y3-y4)/(x3-x4)
	b2 = y3 - a2*x3
	img = np.array(img)
	for x in range (colunas-1): #colunas
		
		posY =int( (a*x+b) )
		posY2 =int( (a2*x+b2) )
		#print(x,posY)
		if((posY<linhas) ): #descending curve, inverse
			img[x][:posY] = np.zeros(posY)
			
		if((posY2<linhas)):
			img[x][posY2:] = np.zeros(linhas-posY2)
	cv2.imwrite (img_path,img)
	

	


