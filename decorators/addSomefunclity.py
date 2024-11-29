def new_pretty(func):
  def new_inner():
    print("hi, I got decorated")
    func()

  return new_inner

def theNormal():
  print("Hi, I'm theNormal")



pret1 = new_pretty(theNormal)
pret1()