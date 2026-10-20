import numpy as np

def make_windows(series, window, horizon, stride=1):
    """
    Returns (X, Y): X (n_windows, window), Y (n_windows, horizon).
    Empty arrays with shapes (0, window) and (0, horizon) if the series is too short.
    """
    # Your code here
    series = np.asarray(series)
    T = len(series)

    n_window = (T-window-horizon)// stride+1

    if n_window <=0:
        return(
            np.empty((0,window),dtype= series.dtype),
            np.empty((0,horizon),dtype = series.dtype)

        )

    X = np.empty((n_window,window),dtype =series.dtype)
    Y = np.empty((n_window,horizon),dtype =series.dtype)

    for i in range(n_window):
        start = i*stride
        X[i]=series[start:start+window]
        Y[i] = series[start+window : start+window+horizon]

    return X,Y