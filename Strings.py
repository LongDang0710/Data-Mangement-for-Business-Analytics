# 1. Count occurrences of letters 's', 'i', and 'p' in "Mississippi"
word = "Mississippi".lower()

count_s = word.count('s')
count_i = word.count('i')
count_p = word.count('p')

print(f"Count of 's': {count_s}")
print(f"Count of 'i': {count_i}")
print(f"Count of 'p': {count_p}")

# 2. Find the number of characters in word Serendipity? Is there a string 'end' in this word?
word = "Serendipity"

length = len(word)
contains_end = 'end' in word

print(f"Number of characters: {length}")
print(f"Does the word contain 'end'?: {contains_end}")

# 3. Find the first and second occurrence of 'i' in "Mississippi"
word = "Mississippi"

first_occurrence = word.find('i')
second_occurrence = word.find('i', first_occurrence + 1)

print(f"First occurrence of 'i': {first_occurrence}")
print(f"Second occurrence of 'i': {second_occurrence}")

# 4. Find the index of list items containing the substring 'or'
states = ["New York", "New Hampshire", "North Dakota", "Pennsylvania", "North Carolina"]

# Find indexes of states containing 'or'
or_indexes = [i for i, state in enumerate(states) if 'or' in state.lower()]

# Produce subset of states containing 'or'
or_states = [state for state in states if 'or' in state.lower()]

print(f"Indexes containing 'or': {or_indexes}")
print(f"Subset of states containing 'or': {or_states}")


