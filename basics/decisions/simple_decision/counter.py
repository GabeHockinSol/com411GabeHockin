# Gets and sets all three numbers
num1 = int(input("Please enter the first whole number: "))
num2 = int(input("Please enter the second whole number: "))
num3 = int(input("Please enter the third whole number: "))

# varibles to count how many even and odd numbers there are
evenNumberCount = int(0)
oddNumberCount = int(0)

# Find if "num 1" is even or odd
if (num1 % 2) == 0:
   evenNumberCount += 1
else:
   oddNumberCount += 1

# Find if "num 2" is even or odd
if (num2 % 2) == 0:
   evenNumberCount += 1
else:
   oddNumberCount += 1

# Find if "num 3" is even or odd
if (num3 % 2) == 0:
   evenNumberCount += 1
else:
   oddNumberCount += 1

# Display all the numbers outcomes
print("There were " + str(evenNumberCount) + " even and " + str(oddNumberCount) + " odd numbers.")