# display start and end position of the first match occurrence

import re

newtext = "Python is a cross-platform language"
searching = re.search(r"\bP\w+", newtext)
print(searching)
