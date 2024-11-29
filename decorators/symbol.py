def new_pretty(func):
  def new_inner():
    print("hi, I got decorated")
    func()

  return new_inner


# decorating funtion
@new_pretty
def theNormal():
  print("Hi, I'm theNormal")
  

theNormal()