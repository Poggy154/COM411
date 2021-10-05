print("what is your age?")
age = int(input())

if age >= 18:
    print("you are an adult")
elif age >= 13:
    print("you are a teenager")
else:
    print("you are a child")


print("is it sunny?")
is_sunny = input().lower()

print("is it breezy?")
is_breezy = input().lower()

if is_sunny and is_breezy == "yes":
    print("The clothes are dry")
elif is_sunny == "yes" and is_breezy == "no":
    print("the clothes are going to take a while to dry")
else:
    print("the clothes are not dry")


