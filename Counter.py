print("Please enter the first whole number")
x = int(input())
print("Please enter another whole number")
y = int(input())
print(" please enter the third number")
z = int(input())


even = 0
odd = 0

if x % 2 == 0:
    even += 1
else:
    odd += 1

if y % 2 == 0:
    even += 1
else:
    odd += 1
if z % 2 == 0:
    even += 1
else:
    odd += 1

print(f"There are {even} even numbers and {odd} odd numbers")