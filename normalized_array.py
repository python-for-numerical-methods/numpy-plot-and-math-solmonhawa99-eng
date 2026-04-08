import numpy as np

def normalize_array(input_array):
    # במקרה של מערך ריק
    if len(input_array) == 0:
        return []

    # מציאת מינימום
    min_val = input_array[0]
    for x in input_array:
        if x < min_val:
            min_val = x

    # מציאת מקסימום
    max_val = input_array[0]
    for x in input_array:
        if x > max_val:
            max_val = x

    # אם כל הערכים שווים
    if max_val == min_val:
        return [0 for _ in input_array]

    # נרמול
    normalized = []
    for x in input_array:
        x_norm = (x - min_val) / (max_val - min_val)
        normalized.append(x_norm)

    return normalized

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
