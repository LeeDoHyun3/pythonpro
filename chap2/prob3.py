name = input("Hi. What's your name? ")
age = int(input("And how old are you? "))
weigh = int(input("Okay, last question. How many kg do you weigh? "))

dogAge = int(age / 6)
print("\nDid you know taht you're just " , dogAge, " in dog years?\n")

AgeToSeconds = age * 365 * 24 * 60 * 60
print("But you're also ", AgeToSeconds, " seconds old.\n")

print("If a small child were trying to get your attention, your name would become : \n" + (name * 5))

print("\nDid you know that on the moon you would weigh only ", (weigh / 6), " pounds?")
print("But on the sun, you'd weigh " , (weigh * 27.1), " <but, ah... not for long>.\n\n")
print("Press the enter key to exit.")

