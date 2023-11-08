text_file = open("prob3.text", "w")

print("Input your string...")
s = 't'
while(s != 'Q'):
    s = input(">> ")
    if s != 'Q':
        s = s + "\n"
        text_file.write(s)
print("Write process has been finished\n\n\n")

text_file = open("prob3.text", "r")
print("You inputs are below..")
print(text_file.read())


