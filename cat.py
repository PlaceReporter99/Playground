def input(prompt, file):
  print(prompt, end="")
  with open(file) as f:
    print(inn := f.readline())
  return inn
print(input("Enter input: "))
print(input("Enter input: "))
