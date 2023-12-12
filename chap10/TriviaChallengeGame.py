

import shelve

print("\t\tWelcome to Trivia Challenge!\n")
print("\t\tAn Episode You Can't Refuse\n")

questions = shelve.open("trivia.dat")
questions["1"] = ["Which country is the only one to have won a medal at every Olympic Winter Games?", "1. United States", "2. United Kingdom", "3. Germany", "4. Korea", 1]
questions["2"] = ["Which city has hosted both Winter and Summer Olympics?", "1. Turin", "2. Lnnsbruck", "3. Beijing", "4. Japan", 3]
questions["3"] = ["In 2022, 222 athletes competed as part of Team USA in the Winter Olympics. Which state had the highest number of native athletes?", "1. California", "2. Colorado", "3. Minnesota", "4. Maryland", 1]
questions["4"] = ["In Home Alone, where does Kevin’s family end up for the holidays?", "1. Paris", "2. Rome", "3. New York City", "4. Tokyo", 1]

questions.sync()
for key in questions.keys():
    print(questions[key][0], "\n")
    for i in range(4):
        print("\t\t", questions[key][i + 1], "\n")
    answer = int(input("What's your answer?:"))
    if (answer == questions[key][5]):
        print("That's correct!!\n")
    else:
        print("This is a wrong answer\n")

print("Solved all problems")




