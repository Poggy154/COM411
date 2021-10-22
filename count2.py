print("how many live cables should I avoid")
cables_to_avoid = int(input())

cables_avoided = 0

print()

while cables_avoided < cables_to_avoid:
    print("avoiding...", end="\n")
    cables_avoided = cables_avoided + 1
    print(f"Done {cables_avoided} live cables avoided!")
