import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # Your code here
    mean = np.mean(data,axis=0)

    std = np.std(data,axis=0)
    standardized = (data-mean)/std

    covariance = np.cov(standardized,rowvar=False)

    eigen_value,eigen_vector= np.linalg.eig(covariance)

    order = np.argsort(eigen_value)[::-1]
    components = eigen_vector[:,:k]

    for i in range(k):
        for value in components[:,i]:
            if abs(value) > 1e-10:
                if value<0 :
                    components[:, i ]*=-1
                break
    
    return np.round(components,4)