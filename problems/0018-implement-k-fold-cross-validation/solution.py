import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    indices = np.arange(n_samples)

    if shuffle:
        np.random.shuffle(indices)
    
    fold_sizes = np.full(k,n_samples // k,dtype =int)
    fold_sizes[:n_samples % k]+=1

    folds=[]
    start=0

    for size in fold_sizes:
        end =start+size
        folds.append(indices[start:end].tolist())
        start=end

    result=[]

    for  i in range(k):
        test_indices = folds[i]

        train_indices =[]

        for j in range(k):
            if j!=i:
                train_indices.extend(folds[j])

        result.append((train_indices,test_indices))

    return result