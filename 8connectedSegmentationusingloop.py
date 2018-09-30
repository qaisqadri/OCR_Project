''' 
Segmention using loop and queue

'''
import cv2
import numpy as np
import queue

xmin,ymin=7000,7000
xmax,ymax=0,0
pixs=np.array([],dtype='int32')
linepixs=np.array([],dtype='int32')
path="C:/Users/ABC/Desktop/project study/test/test/"
pathchars="C:/Users/ABC/Desktop/project study/test/chars4/"
filename="i2.jpg"
flag=0
space=0
ax,ay=0,0
count=0
img=cv2.imread(path+"i2.jpg",0)
imgOriginal=cv2.imread(path+filename)
sx,sy=img.shape
def getImage():
    global path,sx,sy,img
    
    
    
    r,img=cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    sx,sy= img.shape

    r,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    
    
    kernel = np.ones((1,1),np.uint8)
    img = cv2.dilate(img,kernel,iterations = 1)
    
    r,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    
    #img = cv2.Laplacian(img,cv2.CV_64F)
    cv2.imwrite(path+"blobbed.jpg",img)
    
    
    
    
    

def segments(img,x,y):
    global xmin,ymin,xmax,ymax,pixs,m,flag,linepixs,sx,sy,space,count
    xmin,ymin=img.shape
    xmax,ymax=0,0
    
    q=queue.Queue()
    
    if(img[x][y]==0):
        img[x][y]=50
        
        q.put([x,y])
        
        if(xmin>x ):
            xmin=x
        if(ymin>y):
            ymin=y
        
        while( 1==1 ):
            #print("1==1")
            
            while( y+1<sy and img[x][y+1]==0):
                y=y+1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
            
            if(y>ymax):
                ymax=y
                
            while( y+1<sy and x+1 < sx and img[x+1][y+1]==0):
                y=y+1
                x=x+1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
            
            if(y>ymax):
                ymax=y
            if(x>xmax):
                xmax=x
            
            while(y-1>=0 and img[x][y-1]==0):
                y=y-1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
                    
            while(y-1>=0 and x-1>0 and img[x-1][y-1]==0):
                y=y-1
                x=x-1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
                    
            if(ymin>y):
                ymin=y
            if(xmin>x):
                xmin=x
            
            while(x-1>=0 and img[x-1][y]==0):
                x=x-1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
            if(xmin>x):
                xmin=x
            
            while(x-1>=0 and y+1<sy and img[x-1][y+1]==0):
                x=x-1
                y=y+1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
            
            if(xmin>x):
                xmin=x
            if(y>ymax):
                ymax=y
            
            while(x+1<sx and img[x+1][y]==0):
                x=x+1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
                    
            if(x>xmax):
                xmax=x
                
            while(x+1<sx  and y-1 > 0 and img[x+1][y-1]==0):
                x=x+1
                y=y-1
                if(img[x][y]==0):
                    img[x][y]=50
                    
                    q.put([x,y])
            if(ymin>y):
                ymin=y
                
            if (q.empty()):
                break
            else:
                x,y=q.get()
            
        #outside the 1==1 loop
        
        linepixs=np.append(linepixs,[xmin,ymin,xmax,ymax])        
        
    if (flag==1):
        
        if(linepixs.size>0):
            
            linepixs=linepixs.reshape((int(linepixs.size/4),4))
            linepixs = linepixs[linepixs[:,1].argsort()]
            pixs=np.append(pixs,linepixs)
            linepixs=np.array([],dtype='int32')
            
            
def fixPix():
    global pixs
    
    pixs=pixs.reshape((int(pixs.size/4),4))
        
    return

def makeRects(imgO):
    global pixs, ax,ay
    i=0
    for x in pixs:
        #if( pixs[i][2]-pixs[i][0] > ax/1.5 and pixs[i][3]-pixs[i][1]< ay*5):
            if(x[1]==-1):
                temp=np.zeros((30,30))+255
                cv2.imwrite(pathchars+str(i)+".jpg",temp)
                
            if(x[1]!=-1):
                cropChars(i,x[1]-1,x[3]+1,x[0]-1,x[2]+1)
                #cv2.rectangle(imgO,(x[1]-1,x[0]-3),(x[3]+1,x[2]+3),(0,0,255),1)
                
                #cv2.imshow("tesjkldfgjdfklgjdfklgjdfklgjdfklgjdfklgjsdfkgjsdfjgkdfjgldfjgdfkt",imgO)
                #cv2.namedWindow("output", cv2.WINDOW_NORMAL)
                #cv2.imshow("output", imgO)
                #cv2.waitKey(50)
            
            i=i+1
    cv2.destroyAllWindows()
    cv2.imwrite(path+"result.png",imgO)
    
def findAvgSize():
    global ax,ay,pixs
    for x in pixs:
        
        ax=ax+(x[2]-x[0])
        ay=ay+(x[3]-x[1])
    
    nx,ny=pixs.shape
    ax=ax/nx
    ay=ay/nx

    
def cropChars(c,y1,y2,x1,x2):
    global pathchars,imgOriginal
    
    i=imgOriginal[x1:x2,y1:y2]
    #r,i = cv2.threshold(i,145,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    i=cv2.cvtColor( i, cv2.COLOR_RGB2GRAY )
    
    cv2.imwrite(pathchars+str(c)+".jpg",i)
    
    
def selectSegments():
    global pixs,ax,ay
    i=0
    while(i<int(pixs.size/4)):
        
        if  (not( pixs[i][2]-pixs[i][0] < ax*2 and pixs[i][3]-pixs[i][1] < ay*2 and pixs[i][2]-pixs[i][0] > ax/3 and pixs[i][3]-pixs[i][1] > ay/3)):
            
            pixs= np.delete(pixs, i,  axis=0)
  
        i=i+1
    
    return


def findSpaces():
    global pixs,ax,ay
    
    i=0
    while(i < (pixs.size/4)-1 and (pixs.size/4) > 1):
        if ( abs(pixs[i][3]-pixs[i+1][1]) > ay*0.7 ):
            #pixs=np.insert(pixs,i+1,[pixs[i][0],pixs[i][3]+1,pixs[i][2],5],axis=0)
            pixs=np.insert(pixs,i+1,[-1,-1,-1,-1],axis=0)
            i=i+2
        
        i=i+1

    return
    



def doSegmentation():
    global img,flag,linepixs,sx,sy,imgOriginal,ax,ay,pixs
    
    getImage()
    
    i=sx
    j=sy
    #horizontal checking
    for x in range(0,i-2):
        flag=1  # assuming its a blank row
        ty=1
        while (ty<j-2):
            if (img[x][ty]==0 or img[x][ty]==50):
                flag=0 # no it is not
                break
            ty+=1
            # modify : no need to check the row if flag=0
        for y in range(0,j-2):
            segments(img,x,y)
            
          
    fixPix()
    
    findAvgSize()
    
    #selectSegments()
    
    findSpaces()
    
    
    makeRects(imgOriginal)
    
    return


doSegmentation()