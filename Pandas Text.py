import pandas as pd

# 1. Construct a dataframe using two series
s1 = pd.Series([' New York', 'North Carolina ', 'South Dakota'])
s2 = [7, 10, 3]
df = pd.DataFrame({'Statex ': s1, ' X var': s2})

# Remove white space from the first column
df['Statex '] = df['Statex '].str.strip()
print(df)

# 2. Correct the name for the first column using the replace function
df.columns = df.columns.str.replace('Statex ', 'State', regex=False)
print(df)

# 3. Remove spaces between words in the first column using the replace function
df['State'] = df['State'].str.replace(' ', '', regex=False)
print(df)

# 4. Create a new column containing the number of letters in each state name
df['LetterCount'] = df['State'].str.len()
print(df)

# 5. Write a function to retain only the capitalized letters (state abbreviations)
def abbreviate(state_name):
    return ''.join([char for char in state_name if char.isupper()])

df['StateAbbrev'] = df['State'].apply(abbreviate)
print(df)
