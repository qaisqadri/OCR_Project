'''
feature extraction

'''

import cv2
import numpy as np




pathchars="//home//qais//OCRProject//"


features=np.array([],dtype=np.uint8)

def pickChars(path):
    
    global features,pathchars
    features=np.array([],dtype=np.uint8)
    c=0
    while (1==1 ): #erase "and c<10 part"
       #grids=np.array([],dtype='int32')
       # print(c)
       ch=cv2.imread(pathchars+path+'//'+str(c)+".jpg",0)
       if ( ch is None ):
           break

       ht,wd=ch.shape
       size=40
       gridpixs=2
       if(ht>size):
           
           ch=image_resize(ch,height=size-2)
           ht,wd=ch.shape
           
       if(wd>size):
           ch=image_resize(ch,width=size-2)
           ht,wd=ch.shape
           
       r,ch=cv2.threshold(ch,200,255,cv2.THRESH_BINARY)
       
       
       mask=np.zeros((size,size))+255
       xs=int(((size)-ht)/2)
       yt=int(((size)-wd)/2)
       
       mask[xs:xs+ch.shape[0],yt:yt+ch.shape[1]] = ch
       
       
       # feature extraction
       h=0
       w=0
       while(h<size):
           w=0
           while(w<size):
               i=h
               gcount=0
               while(i<h+gridpixs):
                   j=w
                   
                   while(j<w+gridpixs):
                       if(mask[i][j]==0):
                           gcount+=1
                             
                       j=j+1
                       
                   
                   i=i+1
               features=np.append(features,[gcount]) #selected boxes are (h/5,w/5)'s
               #grids=np.append(grids,[(int(h)),(int(w))]) #selected boxes are (h/5,w/5)'s
                   
               w=w+gridpixs
           
           h=h+gridpixs
       '''
       cv2.imwrite(pathchars+str(c)+"m.jpg",mask)
       
       
       mask=cv2.imread(pathchars+str(c)+"m.jpg")
       a=0
       mask2=np.zeros((size,size))+255
       
       grids=grids.reshape((-1,2))
       
       while(a < int(grids.size/2)):
           cv2.rectangle(mask,(grids[a][1],(grids[a][0])),(grids[a][1]+5,(grids[a][0])+5),(0,0,255),1)
           cv2.rectangle(mask2,(grids[a][1],(grids[a][0])),(grids[a][1]+5,(grids[a][0])+5),(0,255,55),1)
           
           a=a+1
           
       cv2.imwrite(pathchars+str(c)+"m.jpg",mask)
       cv2.imwrite(pathchars+str(c)+"m2.jpg",mask2)
       
       
       '''
       # print(c)
       c=c+1
       
       
    features=features.reshape((-1,20,20))
    
    return features

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized
if __name__=="__main__":
    f=pickChars('chars')
    print("features : ")
    print(f)


