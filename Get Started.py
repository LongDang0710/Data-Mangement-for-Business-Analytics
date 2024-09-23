# 1. Create a variable t7 containing the string Bond_Movie_14
t7 = "Bond_Movie_14"
print(t7)

# 2. Create the same variable as the sum of the three words within it
t7_sum = "Bond" + "_" + "Movie" + "_" + "14"
print(t7_sum)

# 3. What is the remainder when you divide 18 by 5?
remainder = 18 % 5
print(remainder)

# 4. alculate the payment for a 36-month loan for $25,000 at a monthly rate of 0.5%
Amt = 25000
r = 0.005
N = 36

PMT = (Amt * r) / (1 - (1 + r) ** -N)
print(PMT)
