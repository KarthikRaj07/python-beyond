# Global variable using global key

def newfunc():
  global i
  i = 50
  print(i)


newfunc()
print(i+7)