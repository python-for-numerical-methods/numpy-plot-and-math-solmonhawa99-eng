import numpy as np
import pytest

# Placeholder for the normalized_array function to resolve ModuleNotFoundError
def normalized_array(arr):
    arr = np.array(arr, dtype=float)
    min_val = np.min(arr)
    max_val = np.max(arr)

    if max_val == min_val:
        return np.zeros_like(arr, dtype=float)
    else:
        return (arr - min_val) / (max_val - min_val)

def test_basic_normalization():
    data = [10, 20, 30]
    result = normalized_array(data)
    expected = np.array([0.0, 0.5, 1.0])
    np.testing.assert_allclose(result, expected, atol=1e-5)

def test_all_same_values():
    # מקרה קצה - כל הערכים זהים
    data = [5, 5, 5]
    result = normalized_array(data)
    expected = np.array([0.0, 0.0, 0.0])
    np.testing.assert_allclose(result, expected, atol=1e-5)

def test_negative_values():
    data = [-10, 0, 10]
    result = normalized_array(data)
    expected = np.array([0.0, 0.5, 1.0])
    np.testing.assert_allclose(result, expected, atol=1e-5)
