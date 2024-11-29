# Yeilding the square of a number

def squaredSeqence(i):
  for x in range(i):
    yield x * x

  newGenera = squaredSeqence(6)
  while True:
    try: 
      
      print("Received on next(): ", next(newGenera))
    
    except StopIteration:
      break