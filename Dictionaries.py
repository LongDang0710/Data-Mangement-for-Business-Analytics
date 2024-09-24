# 1. Make a dictionary with letters in the word 'mississippi' and their frequency
word = 'mississippi'
frequency = {}

for letter in word:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

print(frequency)

# 2. Make a dictionary with keys 1:10 and values equal to twice the value of the key. Iterate over this and sum the values where the key is an odd number
# Create dictionary with keys 1 to 10 and values twice the key
numbers = {i: i * 2 for i in range(1, 11)}

# Sum the values where the key is odd
odd_sum = sum(value for key, value in numbers.items() if key % 2 != 0)

print(f"Dictionary: {numbers}")
print(f"Sum of values for odd keys: {odd_sum}")
