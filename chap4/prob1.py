import random as r

print("I sense our energy. Your ture emotions are coming acroos my screen.")
print("You are...")
mood = r.randrange(3)

if mood == 0:
  print("\t\t-------------------")
  print("\t\t|                 |")
  print("\t\t|  O           O  |")
  print("\t\t|       <         |")
  print("\t\t|                 |")
  print("\t\t|  \          /   |")
  print("\t\t|   \________/    |")
  print("\t\t-------------------")
elif mood == 1:
  print("\t\t-------------------")
  print("\t\t|                 |")
  print("\t\t|  O           O  |")
  print("\t\t|       <         |")
  print("\t\t|                 |")
  print("\t\t|    ---------    |")
  print("\t\t|                 |")
  print("\t\t-------------------")
elif mood == 2:
  print("\t\t-------------------")
  print("\t\t|                  |")
  print("\t\t|  O           O   |")
  print("\t\t|       <          |")
  print("\t\t|                  |")
  print("\t\t|     ______       |")
  print("\t\t|    /      \      |")
  print("\t\t-------------------")
else:
  print("Illegal mood value!")

print("\n...today")


