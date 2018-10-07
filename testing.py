
def predict(features,classifier):
	from sklearn.externals import joblib
	
	if classifier=='KNN':
		clf = joblib.load('clsfKNN.pkl')
	elif classifier=='CNN':
		clf = joblib.load('clsfCNN.pkl')
	elif classifier == 'SVM':
		clf= joblib.load('clsfSVM.pkl')
	elif classifier == 'TREE':
		clf= joblib.load('clsfTREE.pkl')

	print("classifier : ",classifier)
	features=features.reshape((-1,200))
	#print(features.shape)
	result=clf.predict(features)
	#print('Result : ')
	fr=''
	for x in result:
		fr=fr+str(x)

	print(fr)
	


