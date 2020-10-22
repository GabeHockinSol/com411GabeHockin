# Gets and stores number 1
num1 = float(input("Please enter the first number: "))
# Get and stores number 2
num2 = float(input("Please enter the second number: "))

if (num1 < num2):
  print("The first number is the smallest!")
elif (num1 > num2):
  print("The second number is the smallest!")
else:
  print("Both are equal!")