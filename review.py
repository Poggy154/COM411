print("What is your favourite type of music?")
music = input()

if music == "rap":
    print("What style of rap? hip-hop or grime?")
    rap = input()
    print("Fast or slow?")
    speed = input()
    if (rap == "hip-hop") and (speed == "fast"):
        print("Noice, i like that style too")
    elif (rap == "grime") and (speed == "fast"):
        print("oooo how fun")
    elif(rap == "hip-hop") and (speed == "slow"):
        print("Ahh slow rap.")
    elif (rap == "grime") and (speed == "slow"):
        print("Nice style")
    else:
        print("I do not know that style")
elif music == "rock":
    print("What style of rock? heavy metal or moderate?")
    rock = input()
    print("screaming or a mix of rap?")
    style = input()
    if (rock == "heavy metal") and (style== "screaming"):
        print("ahh thats a bit loud, i may go deaf")
    elif (rock == "heavy metal") and (style == "rap"):
        print("oooo how fun")
    elif (rock == "moderate") and (style == "screaming"):
        print("Ahh a mixture, how original")
    elif (rock == "moderate") and (style == "rap"):
        print("Nice style")
    else:
        print("I do not know that style")
elif music == "pop":
    print("What style of pop? just singing or with a bit of rap?")
    pop = input()
    print("slow or fast")
    style = input()
    if (pop == "singing") and (style == "slow"):
        print("nice, that way, you'll be able to listen to it carefully")
    elif (pop == "rap") and (style == "fast"):
        print("oooo how fun")
    elif (pop == "singing") and (style == "fast"):
        print("Ahh a mixture, how original")
    elif (pop == "rap") and (style == "slow"):
        print("Nice style")
    else:
        print("I do not know that style")
else:
    print("Ahh I am not too sure on that style, i'll have to give it a go.")