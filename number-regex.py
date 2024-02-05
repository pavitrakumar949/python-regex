import re

pattern = "[0-9]"

print("Enter a number here: ")
text= input()

if re.search(pattern,text):
    print("pattern got matched")
else:
        print("pattern didnt match")
