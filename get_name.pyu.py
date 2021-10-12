def get_name():
    print("Please enter your name")
    name = input()
    return name

def display_name():
    print(f"***{get_name()} ***")

name = get_name()
display_name()

print(get_name())
