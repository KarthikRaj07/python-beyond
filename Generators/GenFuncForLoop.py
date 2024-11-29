# using generator with for loop

def upTo(i):
  for x in range(i):
    yield x


newseq = upTo(4)

print(next(newseq)) #0
print(next(newseq)) #1
print(next(newseq)) #2
print(next(newseq)) #3
print(next(newseq)) #StopIteration
