# Create a datframe using: np.random.randn(8,4), columns=list('ABCD') (set seed to 9 before doing this)
import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(9)

# Create a dataframe with random values
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)

# 1. View the first two observations.
# View the first two rows without using .head()
print(df.iloc[:2])

# 2. View a slice comprising of rows with labels '2' and '3' and columns A & C
# Select rows 2 and 3, and columns A and C
subset = df.loc[2:3, ['A', 'C']]
print(subset)

# 3. Obtain scalar value in location (7 x 3)
# Get the scalar value at position (7, 3)
scalar_value = df.iloc[7, 3]
print(scalar_value)

# 4. Obtain all observations in dataframe in which the values of both "A" and "D' are more than 0
# Filter the dataframe where both A and D are greater than 0
filtered_df = df[(df['A'] > 0) & (df['D'] > 0)]
print(filtered_df)
