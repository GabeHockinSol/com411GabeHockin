# the user is prompt a question and the answer is stored to the "num" varible
num = int(input("Please enter a whole number: "))

# this does a check to see if the number is even, if divison by 2 gives a remainder of 0. Then check if the remainder is 1, then it is an odd number.
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))