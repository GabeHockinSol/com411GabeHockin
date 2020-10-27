import random
RandMessage = int((random.choice([0, 1, 2, 3])))

# gives us a the same message but written differently
if(RandMessage == 0) or (RandMessage == 2):
  userColour = str(input("Choose one of the two colours (red, blue): "))
  userNumber = str(input("Now choose one of the two numbers (1, 2): "))
else:
  userNumber = str(input("Choose one of the two numbers (2, 1): "))
  userColour = str(input("Now Choose one of the two colours (blue, red): "))

# Message
print("I am now going to guess your answer through trial and error")

# Guessing
if(userColour == "red") and (userNumber == "1"):
  print("You chose red and 1")
elif(userColour != "red") or (userNumber == "1"):
  if(userColour == "blue") and (userNumber == "1"):
    print("You chose blue and 1")

elif(userColour == "red") and (userNumber != "1"):
  print("You chose red and 2")  
if(userColour != "red") or (userNumber != "1"):
  if(userColour == "blue") and (userNumber == "2"):
    print("You chose blue and 2")
