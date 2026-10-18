import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	y_true = np.array(y_true,dtype = int)
	y_pred = np.array(y_pred,dtype=int)

	correct =np.sum(y_true==y_pred)

	output = correct/len(y_pred)

	return output