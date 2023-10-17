import random

word = ["PYTHON", "APPLE", "BANANA", "Daegu", "catholic", "university"]
w = random.choice(word)
ww = []
for s in w:
    ww += "-"
uw = []
hman = [" ------", "|", "|", "|", "|", "|", "|", "|", "-----------"]

cnt = 0
while(cnt < 6):
    g = input("\nEnter your guss : ") 
    uw += g
    if g in w :
        print("Yes! ", g, " is in the word!")
        i = 0
        for j in w:
            if g == j:
                ww[i] = j
            i += 1

    else:
        print("No. ", g, " is not in the word.")
        cnt += 1
        if cnt == 1:
            hman[1] += "      |"
        if cnt == 2:
            hman[2] += "      O"
        if cnt == 3:
            hman[3] += "   ---|---"
        if cnt == 4:
            hman[4] += "      |"
        if cnt == 5:
            hman[5] += "     / \\"
        if cnt == 6:
            hman[6] += "    |   |" 
    for hm in hman:        
        print(hm, "\n")

    if cnt == 6:
        print("LOSE")
        break


    print("You've used the following letters:\n", uw, "\n")
    print("So far, the word is : ")

    for s in ww:
        print(s, end = "")
    
    if "-" not in ww:
        print("\n\nWIN")
        break


