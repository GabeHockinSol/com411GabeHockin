phrase = str(input("Please enter phrase \n"))

# finds how many characters are in the phrase by using the len() function
charCount = int(len(phrase))
#stores current count
currentCount = int(0)

while (currentCount < charCount):
  currentCount = currentCount + 1
  print("Bop ", end="") # using end="" keeps it all on the same line