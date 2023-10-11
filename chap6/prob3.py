geek = {"404" : "clueless.", "Uninstaled" : "being fired.", }
i = 1
while(i != 0):
    print("\n\tGeek Translator\n")
    print("0 - Quit")
    print("1 - Look Up a Geek Term")
    print("2 - Add a Geek Term")
    print("3 - Redefine a Geek Term")
    print("4 - Delete a Geek Term")

    i = int(input("Choice : "))
    if i == 1:
        t = input("\nWhat term do you want me to transate?: ")
        if t in geek:
            print(geek.get(t))
        else:
            print("Unstaled means being fired. Especially popular during the dot-bomb era.")
    elif i == 2:
        t = input("Term : ")
        g = input("Geek : ")
        geek[t] = g
    elif i == 3:
        t = input("\nWhat term do you want me to transate?: ")
        s = input("Geek : ")
        if t in geek:
            geek[t] = s
        else:
            print("Unstaled means being fired. Especially popular during the dot-bomb era.")    
    elif i == 4:        
        t = input("\nWhat term do you want me to transate?: ")  
        if t in geek:
            del(geek[t])
        else:
            print("Unstaled means being fired. Especially popular during the dot-bomb era.")
    

