maxCables = int(input("How many live cables should I avoid? \n"))

# To keep track of how many cables we are on
currentCables = int(0)

# loop has started
while (currentCables < maxCables):
  currentCables = currentCables + 1
  print("Avoiding...Done! " + str(currentCables) + " live cables avoided.")

# loop has finished
print("All cables avoided!")