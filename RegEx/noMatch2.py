#If no matches are found, the value none is returned

import re
  
newtext = "The rain in Germany and spain"
matching = re.findall("Brazil",newtext)

print(matching)