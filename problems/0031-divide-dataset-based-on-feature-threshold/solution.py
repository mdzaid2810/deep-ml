import numpy as np

def divide_on_feature(X, feature_i, threshold):
    X = np.array(X)

    right_mask = X[:, feature_i] >= threshold
    left_mask = X[:, feature_i] < threshold

    X_right = X[right_mask]
    X_left = X[left_mask]

    return X_right, X_left