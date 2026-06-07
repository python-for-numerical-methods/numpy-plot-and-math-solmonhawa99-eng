import numpy as np

def normalized_array(input_array):

    min_val = np.min(input_array)
    max_val = np.max(input_array)

    if min_val == max_val:
        new_array = np.zeros_like(input_array, dtype=float)
    else:
        new_array = (input_array - min_val) / (max_val - min_val)

    return new_array
