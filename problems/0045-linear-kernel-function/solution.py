import numpy as np

def kernel_function(x1, x2):
	# Your code here
	x1 = np.array(x1,dtype =int)
	x2 =np.array(x2,dtype = int)

	result = np.dot(x1,x2)

	return result
