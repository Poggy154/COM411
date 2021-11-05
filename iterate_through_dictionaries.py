def pattern():
    sequences = {"short sequence":3,"medium sequence":2, "Long sequence":1}
    return sequences

def display_keys(data):
   print("Keys:")
   for key in data:
       print(key)
    print()

def display_values(data):
    print("Values:")
    for value in data.value():
        print(value)
    print()

def display_pairs(data):
    print("Pairs:")
    for key, value in data:
        print(f"{key}: {value}")
    print()

def run():
    data = pattern()
    print(f"Dictionary:\n{data}")

    display_keys(data)
    display_values(data)
    display_pairs(data)
