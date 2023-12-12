try:
    num = float(input("Enter a number: "))
except:
    print("Soemthing went wrong!")

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("That was not a number!\n")

for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end = "")
        print(float(value))
    except(TypeError, ValueError):
        print("Someting went wrong!")

print("\n")
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "-->", end = "")
        print(float(value))
    except(TypeError):
        print("I can only convert string or number!")
    except(ValueError):
        print("I can only convert string of digit!")

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("Not a number! Or as Python would say:")
    print("invalid literal for float<> : Hi!\n")

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("That was not a number!")
else:
    print("You entered the number", num)
    


