# 1. Read one of the many csv files provided. View the first 10 observations
import pandas as pd

# Assuming 'your_file.csv' is available in the working directory
df = pd.read_csv(r"F:\Master Resources\BANA.680.01 - Data Mgmt for Business Analyst\Week 4\Auditor Data.csv")

# View the first 10 observations
print(df.head(10))

# 2. How many variables are there in this dataframe?
# Count the number of columns (variables) in the dataframe
num_variables = len(df.columns)
print(f"Number of variables: {num_variables}")

# 3. What is the 75th percentile value of the first numeric variable in the dataframe?
# Select the first numeric column in the dataframe
first_numeric_col = df.select_dtypes(include=['number']).iloc[:, 0]

# Calculate the 75th percentile
percentile_75 = first_numeric_col.quantile(0.75)
print(f"75th percentile of the first numeric variable: {percentile_75}")
