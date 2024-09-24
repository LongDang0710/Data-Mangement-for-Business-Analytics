# 1. Locate index and value where the cumsum is for the first time at least 10
import numpy as np

z1 = np.arange(1, 12, 2).reshape(3, 2)
cumsum_z1 = np.cumsum(z1)
index = np.argmax(cumsum_z1 >= 10)  # Find the index where cumsum is at least 10
value = cumsum_z1[index]

print(f"Index: {index}, Value: {value}")

# 2. Print the difference between the max and min values of each row
row_diff = z1.max(axis=1) - z1.min(axis=1)
print(row_diff)

# 3. print the cumsum of each column
col_cumsum = np.cumsum(z1, axis=0)
print(col_cumsum)

# 4. Create a 4 by 5 array containing random normal values with a mean of 5 and a sigma of 2
random_array = np.random.normal(loc=5, scale=2, size=(4, 5))
print(random_array)
