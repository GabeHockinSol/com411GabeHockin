# Introduction and prompt the user for an input
totalSumNumbers = int(input("How many numbers should I sum up? \n"))

# stores the current number
currentNumber = int(0)
# stores the input number and the total number, so we can add the values to get our answer
userNumber = float(0)
totalNumber = float(0)

# keeps prompting the user for a new number until we have reached the "totalSumNumbers"
while(currentNumber < totalSumNumbers):
  currentNumber += 1
  print("Please enter number " + str(currentNumber) + " of " + str(totalSumNumbers))
  userNumber = float(input())
  totalNumber = totalNumber + userNumber

# print the answer
print ("The answer is " + str(totalNumber))