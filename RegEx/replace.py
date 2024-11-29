# replacing the match with the  text of your choice


import re

newtext = "Python is a cross-platform language"
matching = re.sub(r"\s", "9", newtext)

print(matching)  #Python9is9a9cross-platform9language