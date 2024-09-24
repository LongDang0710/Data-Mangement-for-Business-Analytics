# 1. Create a pandas dataframe with 3 rows and 4 columns with numbers 1...12. Name the columns P, Q, R, and S
import pandas as pd

# Create a DataFrame with 3 rows and 4 columns
data = {
    'P': [1, 2, 3],
    'Q': [4, 5, 6],
    'R': [7, 8, 9],
    'S': [10, 11, 12]
}
df1 = pd.DataFrame(data)
print(df1)

# 2. Create a pandas dataframe using the first ten business days of 2018 as index and a N(10,3) variable as the only column
import pandas as pd
import numpy as np

# Generate the first 10 business days of 2018
index = pd.date_range('2018-01-01', periods=10, freq='B')

# Generate random numbers with mean 10 and standard deviation 3
data = np.random.normal(10, 3, size=(10, 1))

# Create the DataFrame
df2 = pd.DataFrame(data, index=index, columns=['N(10,3)'])
print(df2)

# 3. Create a pandas dataframe by reading one of the many csv files available to you
import pandas as pd

# Read a CSV file into a DataFrame (assuming 'example.csv' is available in the same directory)
df3 = pd.read_csv(r"F:\Master Resources\BANA.680.01 - Data Mgmt for Business Analyst\Week 4\PopulationUS.csv")

# Show the first few rows of the DataFrame
print(df3.head())
