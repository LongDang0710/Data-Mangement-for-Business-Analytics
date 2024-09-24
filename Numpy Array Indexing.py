# 1. Extract the array
import numpy as np

y = np.arange(35).reshape(5, 7)

# Extracting the array
sub_array_1 = y[[0, 2], [1, 4]]
print(sub_array_1)

# Or use slicing:
sub_array_1_alt = y[::2, 1:5:3]
print(sub_array_1_alt)

# 2. Extract the array
# Extracting the array using slicing
sub_array_2 = y[:, [1, 2, 4]]
print(sub_array_2)

# 3. Show 2 ways to extract the value 25
# First method: using indexing
value_25_1 = y[3, 4]
print(f"First method to extract 25: {value_25_1}")

# Second method: using fancy indexing
value_25_2 = y[3, 4:5][0]
print(f"Second method to extract 25: {value_25_2}")
