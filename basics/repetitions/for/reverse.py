phrase = str(input("What phrase do you see?\n"))

print("Reversing...\n The phrase is: ", end="")

for position in range(len(phrase) -1, -1, -1):
  print(phrase[position], end="")