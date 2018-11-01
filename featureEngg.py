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
       # gridpixs=4
       # trial code
       ch=image_resize(ch,height=size-2) #erased -2
       ht,wd=ch.shape
       if wd>size:
        ch=image_resize(ch,width=size) #erased -2
       ht,wd=ch.shape

       
       # ch=image_resize(ch,width=size)
       # ht,wd=ch.shape

       #upto here

       # if(ht>size):
           
       #     ch=image_resize(ch,height=size) #erased -2
       #     ht,wd=ch.shape
           
       # if(wd>size):
       #     ch=image_resize(ch,width=size)
       #     ht,wd=ch.shape
           
       r,ch=cv2.threshold(ch,200,255,cv2.THRESH_BINARY_INV)

       # TODO: add blurring
       # ch = cv2.adaptiveThreshold(ch,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C ,cv2.THRESH_BINARY,21,5)

       
       
       mask=np.zeros((size,size))
       xs=int(((size)-ht)/2)
       yt=int(((size)-wd)/2)
       
       mask[xs:xs+ch.shape[0],yt:yt+ch.shape[1]] = ch
       # cv2.imwrite('feout/'+str(c)+'.jpg',ch)

       cv2.imwrite('feout2/'+str(c)+'.jpg',mask)
       mask=mask.reshape(1,-1)
       features=np.append(features,mask) #selected boxes are (h/5,w/5)'s
               #grid
       # cv2.imwrite(pathchars+path+'//'+str(c)+"m.jpg",mask)
       
       # print('m',str(c))
       # mask=cv2.imread(pathchars+path+'//'+str(c)+"m.jpg")
      
       # r=0
       # s=0
       # for a in range(10):
       #     for b in range(10):
       #         cv2.rectangle(mask,(b+r,a+s),(b+r+gridpixs,a+s+gridpixs),(0,0,255),1) # 0,0  4,4 /  0,4  8,4 ,  
       #         r=r+gridpixs
               
       #     s=s+gridpixs
       #     r=0

       
       # r=0
       # s=0
       # a=0
       # b=0
     
       # while b<40:
       #  cv2.line(mask,(b,0),(b,39),(0,0,255),1)
       #  cv2.line(mask,(0,b),(39,b),(0,0,255),1)
        
       #  b=b+4

       # a=a+4
       # cv2.imwrite(pathchars+path+'//'+str(c)+"m.jpg",mask)
       # print('mm',str(c))
       # print(str(c))
       c=c+1

              
    features=features.reshape(-1,40*40)
    # print(features.shape)
    
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


