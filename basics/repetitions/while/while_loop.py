maxCables = int(input("How many cables should I remove? \n"))

# To keep track of how many cables we are on
currentCables = int(0)

# loop has started
while (currentCables < maxCables):
  currentCables = currentCables + 1
  print("Removed cable")

# loop has finished
print("All cables removed!")