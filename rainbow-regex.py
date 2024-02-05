import re

pattern = "[Vv]iolet|[Ii]ndigo|[Bb]lue|[Gg]reen|[Yy]ellow|[Oo]range|[Rr]ed"

print("Enter the color of a rainbow: ")
text= input()

if re.search(pattern,text):
    print("pattern got matched")
else:
        print("pattern didnt match")
