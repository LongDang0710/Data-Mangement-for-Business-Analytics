# 1. From a sample txt file provided to you (PopulationUS.prn), print out every 10th line. Include the first and last line in printout
file_path = r"F:\Master Resources\BANA.680.01 - Data Mgmt for Business Anlyts\Week 2\PopulationUS.prn"

with open(file_path, 'r') as file:
    lines = file.readlines()

# Print the first line
print(lines[0].strip())

# Print every 10th line
for i in range(9, len(lines), 10):
    print(lines[i].strip())

# Print the last line if it's not already printed
if len(lines) % 10 != 0:
    print(lines[-1].strip())

# 2. Using the same file, get numerical information into a numpy array
import numpy as np

file_path = r"F:\Master Resources\BANA.680.01 - Data Mgmt for Business Anlyts\Week 2\PopulationUS.prn"

# Open the file and read the lines
with open(file_path, 'r') as file:
    lines = file.readlines()

# Skip the header and extract only the numeric data
numeric_data = []
for line in lines[1:]:  # Skip the first header line
    # Split the line by spaces and take only the numeric values
    parts = line.split()
    numeric_values = parts[1:]  # Skip the first part, which is the state name
    numeric_data.append([float(val) for val in numeric_values])

# Convert to NumPy array
data = np.array(numeric_data)

print(data)

