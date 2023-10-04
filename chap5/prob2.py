import random

word = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')

print("Welcome to Word Jumble!")
print("Unscramble the letters to make a word.")
m = random.choice(word)
ms = list(m)
random.shuffle(ms)

print("Humbled word: ", end = " ")
for i in ms:
    print(i, end = "")


g = input("\nYour guess: ")
if g == m:
    print("Congratulations! You guessed the word: " + m)
else:
    print("Sorry, that's not correct. Te word was : " + m)
