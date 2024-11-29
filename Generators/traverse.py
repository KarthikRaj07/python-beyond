# Yeilding the square of a number

def squaredSeqence(i):
  for x in range(i):
    yield x * x

  newGenera = squaredSeqence(6)
  

  for squar in newGenera:
    print(squar)
