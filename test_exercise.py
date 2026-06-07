import numpy as np

def normalized_array(input_array):

    arr = np.array(input_array, dtype=float)

    min_val = np.min(arr)
    max_val = np.max(arr)

    if min_val == max_val:
        return np.zeros(len(arr))

    return (arr - min_val) / (max_val - min_val)
