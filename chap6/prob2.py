
s = []

i = 1
while(i != 0):
    print("\tHigh Score Keeper\n")
    print("\t0 - Quit")
    print("\t1 - List Scores")
    print("\t2 - Add a score\n")
    i = int(input("Choice: "))
    
    if i == 0:
        break;
    elif i == 1:
        print("\nHigh Scores\n")
        print("NAME\tSCORE")
        for score, name  in s:
            print(name, "\t", score)
        print("")
    elif i == 2:
        name = input("What is the player's name?: ")
        score = input("What score did the player get?: ")
        s += [[int(score), name]]
        s.sort(reverse=True)
        print("")
