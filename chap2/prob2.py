print("\n\t\t\t\tTrust Fund Buddy\n")
print("Totals your monthly spending so that your trust fund doesn't run out <and you're forced to get a real job>.\n")
print("Plese enter the requested, monthly costs. Since you're rich, ignre pennies and use dollar amounts.\n\n")

car = int(input("Lamborghini Tune-Ups: "))
rent = int(input("Manhttan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("presonal Guru and Coach: "))
games = int(input("Computer Games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total: ", total)


