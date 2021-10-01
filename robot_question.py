# Gets to know the user more
print("Please tell me your name")
name = input()
print(f"How old are you {name}")
age= input()
print("How tall are you (in meters) ")
height = float(input())

print("how much do you weigh")
weight=float(input())

bmi= weight / height **2

print(f"{name} you are {age} and your bmi is {bmi}")
