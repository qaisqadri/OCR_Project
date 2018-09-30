
import numpy as np


#pathchars="//home//qais//OCRProject//training//"
label=np.array([],dtype=np.uint8)

i=33
j=0
while(j<4):
	if(i in [58,59,95,96,124]):
		i+=1
		continue
	label=np.append(label,i)	
	i=i+1
	if (i== 126):
		i=33
		j=j+1
f=open('labelfile.txt','w')
for x in label:
	f.write(chr(x))

