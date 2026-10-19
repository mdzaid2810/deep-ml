from collections import Counter
def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	if not apples :
		return 0.0;
	counts = Counter(apples)
	n= len(apples)

	return n*n - sum(c*c for c in counts.values())
	