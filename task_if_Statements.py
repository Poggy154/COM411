#find out what book beep is reading

print("IS the book you are reading, an adventure book?")
adventure = input()
if adventure == "yes":
    print("I like adventure books!\n")
    print("\n")
    print("Finished reading book...")
elif adventure == "no":
    print("I will try again\n")
    print("Is it a horror book?")
horror = input()
if horror == "yes":
    print("Oh how thrilling\n")
    print("Finished reading book...\n")
elif horror =="no":
    print("Dammit\n")
    print("I do not know what other books to say, please tell me")
    type = input()
    print(f"AHHH I totally forgot about that, I find {type} books enjoyable")




