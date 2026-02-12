arr = [10, 20, 30, 40, 50]

elem_1 = arr[1]
elem_3 = arr[3]

print(elem_1, elem_3)
last_three = arr[2::]
print(last_three)

import numpy as np
matrix = np.arange(1,17).reshape(4,4)
print(matrix)

second_row = matrix[1]
print(second_row)

third_column = matrix[:, 2]
print(third_column)

bottom_right = matrix[2,4: 2,4]
print(bottom_right)