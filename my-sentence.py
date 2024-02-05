import re

pattern = "^My"

print("Start a sentence with 'My' ")
text= input()

if re.search(pattern,text):
    print("pattern got matched")
else:
        print("pattern didnt match")
