print("Please enter an number")
number = int(input())

count = 0
total = 1

while count < number:
    count = count + 1
    total = total * count

print(f"The factorial is {total}.")