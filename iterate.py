def directions():
    directions = ["Move Forward", "Move Backward", "Turn left", "Turn right"]
    return directions
def menu():
    print("Please select a direction")
    menu = directions()
    for index in range(len(menu)):
        print(f"{index}: {menu[index]}")
def run():
    menu()

run()


