# Search for the first white-space using seach()


import re

newtext =  "The rain in Germany"
searching = re.search(r"\s", newtext)

print("The first white space is located in position", searching.start())