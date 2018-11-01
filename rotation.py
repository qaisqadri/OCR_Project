'''
faster rotation handling
'''

import numpy as np
import cv2
from wand.image import Image
from wand.color import Color




def find_score(arr, angle,wd,ht,bimg):
    #data = cv2.rotate(arr, angle, reshape=False, order=0)
    M = cv2.getRotationMatrix2D((wd/2,ht/2),angle,1)
    data = cv2.warpAffine(bimg,M,(wd,ht))
    
    
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    
    return hist, score


def correct_it(filename):
	
	img=cv2.imread(filename,0)
	if img is None:
		print('Invalid image')
		return
	f=filename
	ht,wd = img.shape
	pix = img.flatten()
	bimg= 1 - (pix.reshape(( ht, wd)) / 255.0)


	
	delta = 1
	limit = 5
	angles = np.arange(-limit, limit+delta, delta)
	scores = []
	for angle in angles:
	    hist, score = find_score(bimg, angle,wd,ht,bimg)
	    #print(hist,score)
	    scores.append(score)

	best_score = max(scores)
	best_angle = angles[scores.index(best_score)]
	print('Best angle: '+str(best_angle) + "  Best score : "+str(best_score))

	img=Image(filename=filename)
	img.rotate(-best_angle,background=Color('rgb(255,255,255)'))
	img.save(filename='rotatedresult.jpg')
	img=cv2.imread('rotatedresult.jpg')
	return img

if __name__=='__main__':
	correct_it(filename='timg/rtest.jpg')

# M = cv2.getRotationMatrix2D((ht/2,wd/2),best_angle,1)
# img = cv2.warpAffine(img,M,(wd,ht))


# img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,cv2.THRESH_BINARY,13,7)


# img=cv2.GaussianBlur(img,(5,5),0)
# r,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# cv2.imwrite(path+"rotatedimage.jpg",img)


