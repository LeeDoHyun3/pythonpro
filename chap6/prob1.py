inventory = ["sword", "armoor", "shield", "healing potion"]

print("Your items:")
for i in inventory:
    print(i)
print("\nPress the enter key to continue.")
print("You have "+ str(len(inventory)) + " items in your possenssion.")

input("\nPress the enter key to continue.")
if "healing potion" in inventory:
    print("You will live to fight another day.\n")

n1 = int(input("Enter the index number for an item in inventory: "))
print("At index "+ str(n1) +" is " + inventory[n1] + "\n")

n2 = int(input("Enter the index number to begin a silce : "))
n3 = int(input("Enter the index number to end the silce : "))
print("inventory[ "+ str(n2) + " : " + str(n3) + " ]\t\t",end = " ")
print(inventory[n2:n3])

input("\nPress the enter key to continue.")
print("You find a chest. It contains: ")
chest = ["gold", "gems"]
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")
print("You trade your sword for a crossbow.")
inventory[0] = "crossbow"
print("Your inventory is now : \n", inventory, "\n")

input("Press the enter key to continue.")
print("You use your gold and gems to buy an orb fo future teling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now : \n", inventory, "\n")

input("Press the enter key to continue.")
print("In a great battle, your shield is destroyed")
del inventory[2]
print("Your inventory is now : \n", inventory, "\n")

input("Press the enter key to continue.")
input("Press the enter key to continue.")
print("Your crossbow and armor arer stolen by thieves.")
del inventory[0:2]
print("Your inventory is now : \n", inventory, "\n")

