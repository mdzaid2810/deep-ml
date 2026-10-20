
import numpy as np
from collections import Counter
def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	y = np.array(y)
	count = Counter(y)

	prob=0
	for c in count.values():
		prob += (c/len(y))**2

	val = 1-prob
	return round(val,3)