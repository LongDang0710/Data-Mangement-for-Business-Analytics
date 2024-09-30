import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'F:\Master Resources\BANA.680.01 - Data Mgmt for Business Analyst\Dataset\Auditor Data.csv'
df = pd.read_csv(file_path)

# 1. Extract 'dltt' and 'at' for 2016, calculate debt_ratio and plot histogram
df_2016 = df[df['fyear'] == 2016][['dltt', 'at']]

# Discard zero and negative values
df_2016 = df_2016[(df_2016['dltt'] > 0) & (df_2016['at'] > 0)]

# Calculate debt ratio
df_2016['debt_ratio'] = df_2016['dltt'] / df_2016['at']

# Filter out extreme values (e.g., filter out the top 1% debt_ratio values)
upper_limit = df_2016['debt_ratio'].quantile(0.99)
df_filtered = df_2016[df_2016['debt_ratio'] <= upper_limit]

# Plot histogram of the filtered debt ratio values
plt.figure(figsize=(10, 6))
df_filtered['debt_ratio'].plot(kind='hist', bins=30, edgecolor='black')
plt.title('Filtered Debt Ratio Histogram')
plt.xlabel('Debt Ratio')
plt.ylabel('Frequency')
plt.show()

# Print descriptive statistics of the filtered debt ratio
print(df_filtered['debt_ratio'].describe())


# Descriptive statistics for debt_ratio
print(df_2016['debt_ratio'].describe())

# 2. Customization of the plot - Line chart
plt.figure(figsize=(12, 8))  # Increase figure size for better visibility

# Sorting the debt ratio to plot a line chart
df_filtered_sorted = df_filtered.sort_values(by='debt_ratio')

# Plotting the line chart of the debt ratio
plt.plot(df_filtered_sorted['debt_ratio'].values, color='skyblue', marker='o', linestyle='-', linewidth=2, markersize=4)

# Customizing the title, labels, and grid
plt.title('Debt Ratio Line Chart (Filtered)', fontsize=20, fontweight='bold', color='darkblue')
plt.xlabel('Index (Sorted Debt Ratio)', fontsize=16, fontweight='bold')
plt.ylabel('Debt Ratio', fontsize=16, fontweight='bold')

# Adjusting grid style
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Customizing tick labels and reducing frequency of xticks
plt.xticks(fontsize=12, rotation=45, color='darkgreen', ticks=range(0, len(df_filtered_sorted), max(1, len(df_filtered_sorted)//15)))  # Reduce number of ticks
plt.yticks(fontsize=12, color='darkgreen')

# Ensure everything fits and labels aren't cut off
plt.tight_layout()

# Display the customized line chart
plt.show()

# Print descriptive statistics of the filtered debt ratio
print(df_filtered['debt_ratio'].describe())

# 3. Extract 2016 'ni' values for specific stocks and plot bar chart
stocks = ['AGCO', 'DE', 'HON', 'STZ', 'CAT']
df_stocks = df[(df['fyear'] == 2016) & (df['tic'].isin(stocks))][['tic', 'ni']]

# Plot bar chart
plt.figure(figsize=(10, 6))
df_stocks.set_index('tic')['ni'].plot(kind='bar', color='green', edgecolor='black')
plt.title('Net Income of Selected Stocks in 2016', fontsize=16)
plt.xlabel('Stock Symbol', fontsize=14)
plt.ylabel('Net Income', fontsize=14)
plt.xticks(rotation=0)
plt.show()
