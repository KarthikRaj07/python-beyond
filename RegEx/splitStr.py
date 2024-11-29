#return a list where the string has been split at each match

import re

newtext = "Python is a cross-platform language"
newmatch = re.split(r"\s",newtext)

print(newmatch)

split1 = re.split(r"\s",newtext, 1)
print(split1)

