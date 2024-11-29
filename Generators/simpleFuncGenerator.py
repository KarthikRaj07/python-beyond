#building a simple generator function
def newgenerator():
  print("First Result")
  yield "first"

  print("Second Result")
  yield 40

  print("Last Result")
  yield 60


gen1 = newgenerator()
print(next(gen1))
print(next(gen1))
print(next(gen1))