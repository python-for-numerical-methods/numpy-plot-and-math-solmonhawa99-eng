import numpy as np

def normalized_array(input_array):

    min_val = input_array.min()
    max_val = input_array.max()

    if max_val == min_val:
        new_array = np.zeros(input_array.shape)

    else:
        new_array = (input_array - min_val) / (max_val - min_val)

    return new_array
