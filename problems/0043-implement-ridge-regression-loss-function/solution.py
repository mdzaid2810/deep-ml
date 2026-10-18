import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	X =np.array(X,dtype=float)
	w =np.array(w,dtype=float)

	y_true = np.array(y_true,dtype=float)

	pred = X @ w

	mse = np.mean((y_true-pred)**2)

	penalty = alpha*np.sum(w**2)

	return mse+penalty
