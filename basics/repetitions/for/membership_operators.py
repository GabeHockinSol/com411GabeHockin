phrase = str(input("What phrase do you see?\n"))

print("Reversing...\n The phrase is: ", end="")

reversed = ""

for letter in phrase:
  reversed = letter + reversed

print(reversed)

