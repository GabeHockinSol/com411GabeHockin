# Asks user for a number
number = int(input ("Please enter a number?\n"))

# Calculate the factorial

count = 0
total = 1

while (count < number):
  count = count + 1
  total = total * count

print("The fractorial is", total)
