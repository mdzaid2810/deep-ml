import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	# Your code here
	n=X.shape[0]

	for start in range(0,n,batch_size):
		end = start+batch_size

		x_batch=X[start:end]

		if y is not None:
			y_batch=y[start:end]
			yield[x_batch.tolist(),y_batch.tolist()]
		else:
			yield x_batch.tolist()
