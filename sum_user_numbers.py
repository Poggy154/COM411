print("how many numbers should I sum up?")
numbers_to_sum = int(input())

numbers_summed = 0

print()
total = 0
while numbers_summed < numbers_to_sum:
    print(f"Please enter number {numbers_summed} of {numbers_to_sum}:")
    number = int(input())
    total = total + number
    numbers_summed = numbers_summed + 1

print(f"The answer is {total}")