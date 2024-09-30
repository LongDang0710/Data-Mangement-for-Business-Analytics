import numpy as np
import pandas as pd

# 1. Create a dataframe using np.random.randn(8,4) with columns as list('ABCD') (Set the seed to 9)
np.random.seed(9)
df = pd.DataFrame(np.random.randn(8, 4), columns=list('ABCD'))

# 2. Get the correlation matrix. Count correlations greater than 0.2 or less than -0.2
corr_matrix = df.corr()
count_corr = ((corr_matrix > 0.2) | (corr_matrix < -0.2)).sum().sum()

# 3. Implement a function to sum the values for each row but only using positive numbers
def sum_positive(row):
    return row[row > 0].sum()

df['SumPos'] = df.apply(sum_positive, axis=1)

# 4. Implement a function to calculate the percent of positive values for each row
def percent_positive(row):
    total = len(row)
    pos_count = (row > 0).sum()
    return (pos_count / total) * 100

df['PercentPositive'] = df.apply(percent_positive, axis=1)

# 5. Implement a lambda function to sum only values greater than 12 for each column
sum_greater_12 = df.apply(lambda col: col[col > 12].sum())

# Output the dataframe and results
print("Dataframe:\n", df)
print("\nCorrelation Matrix:\n", corr_matrix)
print("\nCount of Correlations > 0.2 or < -0.2:", count_corr)
print("\nSum of values greater than 12 for each column:\n", sum_greater_12)
