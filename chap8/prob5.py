try:
    num = float(input("Enter a number: "))
except:
    print("Soemthing went wrong!")

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("That was not a number!")

for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "->", end = "")
        print(float(value))
    except(TypeError, ValueError):
        print("Someting went wrong!")
print("\n")
for value in (None, "Hi!"):
    try:
        print("Attempting to convert", value, "->", end = "")
        print(float(value))
    except(TypeError):
        print("Can only convert string or number!")
    except(ValueError):
        print("Can only convert string of digit!")

try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("Not a number! Or as Python would say\n")
    
try:
    num = float(input("\nEnter a number: "))
except(ValueError):
    print("That was not a number!")
else:
    print("You entered the number", num)
    


