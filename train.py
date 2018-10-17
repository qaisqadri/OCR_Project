import numpy as np
def training(feat,labelfile,cls):
	feat=feat.reshape((-1,100))
	
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
	print(feat[1].reshape(10,10),labels[1])
	
	if cls=='KNN':
		from sklearn.neighbors import KNeighborsClassifier
		clf = KNeighborsClassifier(n_neighbors=5)
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


