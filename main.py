import segment
# import featureExtractionmoments as fe
import featureExtraction as fe
import train
import testing
import numpy as np


# obj=segment.Segmentation()
# for x in range(0,21):
# 	print(x)
# 	obj.doSegmentation(filename='source/out'+str(x)+'.jpg',size_thresh=250)
# obj.doSegmentation(filename='timg/i1.jpg',size_thresh=250)

classifier='KNN' # can be KNN CNN or SVM
features=fe.pickChars(path='training2') #training data feature extraction

features=features.reshape((-1,100))
	
features.dump('features.txt')


features=np.load('features.txt') # training data features
print('train')

train.training(features,'ll.txt',classifier)

features2=fe.pickChars(path='chars')

testing.predict(features2,classifier)

