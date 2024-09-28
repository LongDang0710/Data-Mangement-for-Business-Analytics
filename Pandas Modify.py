# Create a dataframe using: np.random.randn(8,4), columns=list('ABCD') (set seed to 9 before doing this)
import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(9)

# Create the dataframe with random values
df = pd.DataFrame(np.random.randn(8, 4), columns=list('ABCD'))
print(df)

# 1. Modify the value in position (3,2) to 0
# Modify the value at position (3, 2) to 0
df.iloc[3, 2] = 0
print(df)

# 2. Insert column 'E' which is the sum of A-D
# Add a new column 'E' that is the sum of columns A-D
df['E'] = df.sum(axis=1)
print(df)

# 3. Replace any value >2 or <2 with NaN
# Replace values greater than 2 or less than -2 with NaN
df = df.where((df < 2) & (df >
                          -2), np.nan)
print(df)

