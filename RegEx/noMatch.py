

import re
  
newtext = "The rain in Germany and spain"
x = re.findall("Brazil",newtext)

print(x)
if x:
  print("Match")
else:
  print("Not Match")