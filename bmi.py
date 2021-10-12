def get_name():

    print("Please enter your name")
    name = input()

    print("Please enter your weight")
    weight = float(input())

    print("Please enter your height")
    height = float(input())

    bmi = weight / (height ** 2)
    print(f"Your BMI is {bmi}")
