print("Please enter the first number")
first = int(input())
print("please enter the second number")
second = int(input())

if first > second:
    print("The second number is the smallest")
elif second > first:
    print("the first number is smaller")
elif second == first:
    print("The numbers are the same")
