# 1. Create a list called m1 containing numbers 3...12
m1 = list(range(3, 13))
print(m1)

# 2. Create a shallow copy of m1 and call it m2
m2 = m1[:]
print(m2)

# 3. Modify m2 to contain (3,4,5,6,10,11,12)
m2 = [3, 4, 5, 6, 10, 11, 12]
print(m2)

# 4. Loop through m1 and create list m3 containing only odd numbers in the list
m3 = [num for num in m1 if num % 2 != 0]
print(m3)

# 5. Loop through m3 to calculate the squared value of each element and find the sum
squared_sum = sum([num ** 2 for num in m3])
print(squared_sum)

