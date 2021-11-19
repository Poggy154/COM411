print("how many bars should be charged")
charged = int(input())

be_charged = 0

print()

while be_charged < charged :
    be_charged = be_charged + 1
    print(f"charging: {'█' * be_charged}")

print("the battery is fully charged.")