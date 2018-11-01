import numpy as np
def training(feat,labelfile,cls):
	# feat=feat.reshape((-1,100))
	
	# feat.dump('featureVector.txt')
	
	f=open(labelfile,'r')
	labels=list(f.read())
	f.close()


	from random import shuffle

	ind_list = [i for i in range(len(labels))]
	shuffle(ind_list)
	f  = feat[ind_list]
	l = [labels[i] for i in ind_list]
	
	feat=f
	labels=l
	print(feat[1],labels[1])
	
	if cls=='KNN':
		from sklearn.neighbors import KNeighborsClassifier
		clf = KNeighborsClassifier(n_neighbors=11)
		# feats=feats.reshape(-1,40*40)
		clf.fit(feat, labels) 
	
		from sklearn.externals import joblib
		joblib.dump(clf, 'clsfKNN.pkl')


	elif cls=='CNN':
		from sklearn.neural_network import MLPClassifier
		X = feat/255.0
		X = X.reshape(-1,40,40)
		y = np.array(labels)
		y = y.reshape(-1,1)

		from sknn.mlp import Classifier, Convolution, Layer

		clf = Classifier(
		    layers=[
		        Convolution("Rectifier", channels=89, kernel_shape=(3,3)),
		        Layer("Softmax")],
		    learning_rate=0.02,
		    n_iter=25)
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

	elif cls=='TREE' :
		from sklearn import tree
		clf = tree.DecisionTreeClassifier()
		clf = clf.fit(feat, labels)

		from sklearn.externals import joblib
		joblib.dump(clf, 'clsfTREE.pkl')

	elif cls=='NB' :
		from sklearn.naive_bayes import MultinomialNB
		clf = MultinomialNB()
		clf.fit(feat, labels)

		from sklearn.externals import joblib
		joblib.dump(clf, 'clsfNB.pkl')


