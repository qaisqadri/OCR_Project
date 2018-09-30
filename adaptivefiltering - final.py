
import cv2
import numpy as np
#from matplotlib import pyplot as plt
#from PIL import ImageFilter
#from PIL import Image

path="C:\\Users\\ABC\\Desktop\\project study\\test\\test\\"
img = cv2.imread(path+"i.jpg",0)

#img=cv2.GaussianBlur(img,(3,3),0)

ret,th1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,\
            cv2.THRESH_BINARY,13,7)

#denoisedb = cv2.GaussianBlur(th1,(3,3),0)


#denoisedag = cv2.GaussianBlur(th3,(3,3),0)

cv2.imwrite(path+"bg.jpg",th1)

cv2.imwrite(path+"agg.jpg",th3)
'''
ret,th1 = cv2.threshold(denoisedag,145,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
r,th1 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8)
#erosion = cv2.erode(th1,kernel,iterations = 1)

th1 = cv2.dilate(th1,kernel,iterations = 1)

r,th1 = cv2.threshold(th1,127,255,cv2.THRESH_BINARY_INV)


t=th1

th3=cv2.GaussianBlur(th3,(5,5),0)
r,th3 = cv2.threshold(th3,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
r,th3 = cv2.threshold(th3,127,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((3,2),np.uint8)
th3 = cv2.dilate(th3,kernel,iterations = 1)
r,th3 = cv2.threshold(th3,127,255,cv2.THRESH_BINARY_INV)
r,th3=cv2.threshold(th3,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

'''

th3=cv2.GaussianBlur(th3,(5,5),0)
r,th3 = cv2.threshold(th3,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite(path+"aggb1.jpg",th3)


'''
equ = cv2.equalizeHist(t)
res = np.hstack((t,equ)) #stacking images side-by-side
cv2.imwrite(path+'agg2.jpg',equ)
'''
#im=Image.open(path+"agg.jpg")
#im2=im
#im1 = im.filter(ImageFilter.SMOOTH_MORE)
#im1 = im1.filter(ImageFilter.SMOOTH_MORE)
#im1 = im1.filter(ImageFilter.SMOOTH)
#im1 = im1.filter(ImageFilter.SHARPEN)
#im1 = im1.filter(ImageFilter.SHARPEN)
#im1.save(path+"agblurred1.jpg")

#im2=cv2.imread(path+"agblurred.jpg",0)
#r,t = cv2.threshold(im2,145,255,cv2.THRESH_BINARY +cv2.THRESH_OTSU)
#cv2.imwrite(path+"agblurred2.jpg",t)

#denoised3 = cv2.GaussianBlur(th3,(3,3),0) 
#cv2.imwrite(path+"agblurred1gaussian.jpg",denoised3)
#r,t = cv2.threshold(denoised3,145,255,cv2.THRESH_BINARY)
#cv2.imwrite(path+"agblurred2gaussian3.jpg",t)#final



