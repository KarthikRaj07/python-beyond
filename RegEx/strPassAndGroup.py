# display start and end position of the first match occurrence

import re

newtext = "Python is a Cross-platform language"
searching = re.search(r"\bC\w+", newtext)



print(searching.group())