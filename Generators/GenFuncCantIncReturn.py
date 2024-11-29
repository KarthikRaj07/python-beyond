#building a simple generator function
def newgenerator():
  print("First Result")
  yield 20

  return

  print("Second Result")
  yield 40

  print("Last Result")
  yield 60


gen1 = newgenerator()
print(next(gen1))
