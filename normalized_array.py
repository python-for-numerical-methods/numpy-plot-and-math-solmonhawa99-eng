import numpy as np

def normalized_array(input_array):
  data = input_array.copy()
  data = np.array(data)
  if np.min(data) == np.max(data):
    return np.zeros(data.shape)
  else:
    data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return data

print(normalized_array([5, 5, 5]))
print(normalized_array([-1, 0, 1, 2]))

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
