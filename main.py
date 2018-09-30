import segment
import featureExtraction as fe
import train
import testing
import numpy as np

# obj=segment.Segmentation()
# obj.doSegmentation('rti.png',size_thresh=150)
classifier='KNN' # can be KNN CNN or SVM
# features=fe.pickChars(path='withspaces/finals') training data feature extraction
features=np.load('featureVector.txt') # training data features
print('train')

train.training(features,'withspaces/labeldata.txt',classifier)

features2=fe.pickChars(path='chars')

testing.predict(features2,classifier)









