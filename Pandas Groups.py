import pandas as pd

# Load the dataset from the specified path
file_path = r'F:\Master Resources\BANA.680.01 - Data Mgmt for Business Analyst\Dataset\Auditor Data.csv'
df = pd.read_csv(file_path)

# 1. Form groups by 1-digit SIC and print groups and unique values in groups
df['SIC_1digit'] = df['sic'].astype(str).str[:1]  # Create a 1-digit SIC column
groups = df.groupby('SIC_1digit')
for name, group in groups:
    print(f"Group: {name}")
    print(group['sic'].unique())

# 2. Find the median and max value of the variable 'at' by group (grouped by 1-digit SIC)
median_max_at = groups['at'].agg(['median', 'max'])
print(median_max_at)

# 3. Apply a lambda function to calculate the mean of each group's 'ni' where the minimum value is excluded
def mean_exclude_min(x):
    if len(x) > 1:
        return x[x != x.min()].mean()
    return x.mean()

mean_ni_exclude_min = groups['ni'].apply(mean_exclude_min)
print(mean_ni_exclude_min)

# 4. Filter data to exclude groups with more than 1 negative 'ni' value
filtered_groups = groups.filter(lambda x: (x['ni'] < 0).sum() <= 1)
print(filtered_groups)
