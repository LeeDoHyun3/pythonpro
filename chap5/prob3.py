import random

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's obejective is to guess the chosen word.\n")

w = random.choice(words)
lw = int(len(w))
print("Length of the selected word:" + str(lw))

gw = ""

i = 0
while(lw > i):
    gw += "_"
    i += 1

gw = list(gw)

while(lw > 0):
    print("Remainig attempts: " + str(lw))
    print("Current guessed word: " , end = "")
    for k in gw:
        print(k, end = " ")

    g = input("\nGuess a letter: ")
    if g in w :    
        i = 0
        for k in w:
            if g == k:
                gw[i] = k
            i += 1
    else:
        print("Incorrect guess.")
        lw -= 1
    if gw == list(w):
        print("Congratulations! You guessed the word: " + w)
        break
    elif lw == 0:
        print("You've used up your attempts. The correct word was python.")
