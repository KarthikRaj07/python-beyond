#bulid iterator to return numbers, start from 1, and +1 each sequence

class NewNumber:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 17:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopAsyncIteration

#Create object based on NewwNumbers class  
newclass = NewNumber()
newiter = iter(newclass)

#Display values one by one

for x in newiter:
  print(x)