# 1. Write a function to ask the user for an input number between 10 and 20 and evaluate whether the number is a prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Ask user for input
num = int(input("Enter a number between 10 and 20: "))

if 10 <= num <= 20:
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
else:
    print("Number is not between 10 and 20.")

# 2. Assume that if the weather is sunny ==> play, cloudy ==> work, rainy ==> sleep. Write this as a nested conditional where the variable named weather influences a variable named action
weather = input("Enter the weather (sunny, cloudy, rainy): ").lower()

if weather == "sunny":
    action = "play"
elif weather == "cloudy":
    action = "work"
elif weather == "rainy":
    action = "sleep"
else:
    action = "unknown"

print(f"Action: {action}")

# 3. Write a loop to calculate the sum of square roots for all even numbers between 1 and 20
import math

sum_sqrt = 0
for num in range(2, 21, 2):  # Even numbers between 1 and 20
    sum_sqrt += math.sqrt(num)

print(f"Sum of square roots of even numbers between 1 and 20: {sum_sqrt}")

# 4. Set x1 = 23221.7522. Print it as $23,221.75
x1 = 23221.7522
formatted_x1 = "${:,.2f}".format(x1)
print(formatted_x1)
