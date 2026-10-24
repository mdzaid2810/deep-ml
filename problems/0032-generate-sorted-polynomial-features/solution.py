import numpy as np
from itertools import combinations_with_replacement

def polynomial_features(X, degree):
    X = np.asarray(X)

    n_sample, n_feature = X.shape

    features = []

    features.append(np.ones(n_sample))

    for d in range(1, degree + 1):
        for combination in combinations_with_replacement(range(n_feature), d):
            
            feature = np.prod(X[:, combination], axis=1)
            
            features.append(feature)

    features = np.array(features).T

    features = np.sort(features, axis=1)

    return features