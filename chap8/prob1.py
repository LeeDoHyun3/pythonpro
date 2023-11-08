print("Opening and closing the file.")

text_file = open("prob1.txt", "r")
print("\nReading characters from the file.")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

text_file = open("prob1.txt", "r")
whole_thing = text_file.read()
print("\nReading the entire file at once.")
print(whole_thing)
text_file.close()

text_file = open("prob1.txt", "r")
print("\nReading characters form a line.")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

text_file = open("prob1.txt", "r")
print("\nReadingone line at a time.")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

text_file = open("prob1.txt", "r")
print("\nReading the entire file into a list.")
lines = text_file.readlines()
print(lines)
print(lines[0])
print(lines[1])
print(lines[2])
text_file.close()

text_file = open("prob1.txt", "r")
print("\nLooping throuh the file, line by line.")
for line in text_file:
    print(line)
text_file.close()







