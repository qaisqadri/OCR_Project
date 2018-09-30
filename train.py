import numpy as np
def training(feat,labelfile,cls):
	feat=feat.reshape((-1,64))
	
	# feat.dump('featureVector.txt')
	
	f=open(labelfile,'r')
	labels=list(f.read())
	
	#print(len(labels))
	
	if cls=='KNN':
		from sklearn.neighbors import KNeighborsClassifier
		clf = KNeighborsClassifier(n_neighbors=1)
		clf.fit(feat, labels) 
	
		from sklearn.externals import joblib
		joblib.dump(clf, 'clsfKNN.pkl')


	elif cls=='CNN':
		from sklearn.neural_network import MLPClassifier
		X = feat
		y = labels
		clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2, 2), random_state=1)
		clf.fit(X, y)                         
	
		from sklearn.externals import joblib
		joblib.dump(clf, 'clsfCNN.pkl')

	elif cls=='SVM':

		from sklearn import svm
		clf = svm.SVC()
		X, y = feat, labels
		clf.fit(X, y)  

		from sklearn.externals import joblib
		joblib.dump(clf, 'clsfSVM.pkl')

	f.close()

