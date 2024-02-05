import re

pattern = "s.t"

print("Write any character between 's' and 't' ")
text= input()

if re.search(pattern,text):
    print("pattern got matched")
else:
        print("pattern didnt match")
