import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's obejective is to guess the chosen word.\n")

w = random.choice(words)
i = len(w)
print("Length of the selected word:" + str(i))

gw = ""
i = 0

while(i < len(w)):
    gw += "_"
    i += 1

i = 6
while(i > 0):
    print("Remainig attempts: " + str(i))
    print("Current guessed word: " , end = "")
    j = 0
    while(j < len(gw)):
        print(gw, end = " ")
        j += 1
    g = input("\nGuess a letter: ")
    if g in w :
        j = 0
        while(j < len(w)):
            if(w[j] == g):
                gw[j] = w[j]
    else:
        print("Incorrect guess.")
        i -= 1
    if gw == w:
        print("Congratulations! You guessed the word: " + w)
        break

