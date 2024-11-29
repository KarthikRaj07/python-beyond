#Return a list containing all matches
# 
import re
  
newtext = "The rain in Germany and spain"
x = re.findall("ai",newtext)

print(x)