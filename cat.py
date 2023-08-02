def input(prompt = "", /, file = "stdin.txt"):
  global __incount__
  try:
    __incount__ += 1
  except NameError:
    __incount__ = 0
  print(prompt, end="")
  with open(file) as f:
    try:
      print(inn := f.read().split('\n')[__incount__])
    except IndexError:
      raise EOFError("EOF when reading a line")
  return inn


print(input("Enter input: "))
print(input("Enter input: "))
