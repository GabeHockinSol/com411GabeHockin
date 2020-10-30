rows = int(input("How many rows should I have ?\n"))
columns = int(input("How many columns should I have ? \n"))
print("Here I go: ")

for row in range(0, rows, 1):
  for column in range(0, columns, 1):
    print(":)", end = "")
  print()

"Added code to demonstrate the use of one loop nested is another."