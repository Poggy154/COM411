def get_name():
    print("Please enter your name")
    name = input()
    return name

def get_weight():
    print("please enter your weight")
    weight = float(input())
    return weight

def get_height():
    print("please enter your height")
    height = float(input())
    return height

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def run():
        name = get_name()
        weight = get_weight()
        height = get_height()
        bmi = calculate_bmi(weight, height)
        print(f"{name} your bmi is {bmi}")

if __name__ == "__main__":
    run()