import re

pattern = "^I.+programming$"

print("Write any characters between 'I' and 'programming' and form a sentence ")
text= input()

if re.search(pattern,text):
    print("pattern got matched")
else:
        print("pattern didnt match")
