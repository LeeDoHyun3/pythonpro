class Critter:
    def __init__(self, name, mood_level):
        self.name = name
        self.mood_level = mood_level

    def Talk(self):
        print("I'm", self.name, "and ", end = "")
        m = self.getMood()
        if m == 4:
            print("I feel happy now.\n")
            self.setMood(3)
        elif m == 3:
            print("I feel soso now.\n")
            self.setMood(2)
        elif m == 2:
            print("I feel frustrated now.\n")
            self.setMood(1)
        else:
            print("I feel mad now.\n")

    def Feed(self):
        m = self.getMood()
        if m < 3:
            m += 2
        else:
            m = 4
        self.setMood(m)


    def Play(self):
        self.setMood(4)

    def setMood(self, level):
        self.mood_level = level

    def getMood(self):
        return self.mood_level


name = input("Waht do you wnat to name your critter?: ")
crit1 = Critter(name, 1)

while(True):
    print("\n\t\tCritter Caretaker\n")
    print("\t\t0 - Quit")
    print("\t\t1 - Listen to your critter")
    print("\t\t2 - Feed your critter")
    print("\t\t3 - Play with your critter")
    c = int(input("\nChoice: "))
    print("")
    if c == 1:
        crit1.Talk()
    elif c == 2:
        crit1.Feed()
    elif c == 3:
        crit1.Play()
    elif c == 0:
        break
    else:
        print("Choice 0 ~ 3")















