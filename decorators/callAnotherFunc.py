def calling():
  def returning():
    print("Hello from inner")
  return returning

new = calling()


new()