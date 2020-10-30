maxCharge = int(input("How many bars should be charged? \n"))

# To keep track of how many cables we are on
currentCharge = int(0)

# loop has started
while (currentCharge < maxCharge):
  currentCharge = currentCharge + 1
  print("Charging: "+"◘" * currentCharge)

# loop has finished
print("The battery is fully charged.")