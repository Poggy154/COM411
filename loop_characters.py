print("What strange marking do you see?")
markings = input()

print("\nIdentifying...\n")

for count in range(0, len(markings), 1):
    print(f"index {count}:", markings[count])
