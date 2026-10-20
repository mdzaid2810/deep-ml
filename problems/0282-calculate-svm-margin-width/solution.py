import numpy as np

def svm_margin_width(w: np.ndarray) -> float:
    """
    Calculate the margin width of a linear SVM classifier.
    
    Parameters:
    w : np.ndarray - weight vector defining the hyperplane
    
    Returns:
    float - the total margin width
    """
    w =np.array(w,dtype=float)
    width=0
    for i in w:
        width += i**2

    return 2/np.sqrt(width)