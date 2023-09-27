import random as r

print("Welcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.")

n1 = r.randrange(1, 100)
count = 0
n2 = 0
while(n2 != n1):
    n2 = int(input("Take a guess : "))  
    if (n2 > n1): 
        print("Lower..") 
    elif (n2 < n1):
        print("Higher..")
    count += 1

print("You guessed it! The number was "+ str(n1))
print("And it only took you " + str(count) +" tries!")

