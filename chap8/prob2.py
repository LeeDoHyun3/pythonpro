text_file = open("prob2.text", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()

text_file = open("prob2.text", "r")
print("Creating a text file with the write<> method.\n")
print("Readin the newly created file.")
print(text_file.read())
text_file.close()

text_file = open("prob2_2.text", "w")
lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

text_file = open("prob2_2.text", "r")
print("Creating a text file with the writelinese<> method.\n")
print("Readin the newly created file.")
print(text_file.read())
text_file.close()
