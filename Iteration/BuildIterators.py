#bulid iterator to return numbers, start from 1, and +1 each sequence

class NewNumber:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a += 1
    return x

#Create object based on NewwNumbers class  
newclass = NewNumber()
newiter = iter(newclass)

print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))


