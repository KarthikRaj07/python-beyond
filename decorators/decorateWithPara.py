def best_division(func):
  def inner(x,y):
    print("We're going to divide", x, "and ", y)
    if y == 0:
      print("Sorry, can't divide")
      return
    return func(x,y)
  return inner

@best_division
def division(x,y):
  print(x/y)


division(3,7)
division(3,0)