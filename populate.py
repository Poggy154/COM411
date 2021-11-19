def directions():
    directions = ["Move Forward", "Move Backwards","Turn Left","Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    path = directions()

    for index in range(len(path)):
        print(f"{index}: {path[index]}")
    response = int(input())
    return path[response]


def run():
    route = []
    print("Working out escape route...")
    for index in range(5):
        route.append(menu())
    print(f"Escape route: {route}")

run()


