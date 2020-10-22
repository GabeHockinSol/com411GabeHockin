# prompt the user
print("Towards which direction should I paint (up, down, left or right)?")

# get the user's answer
direction = str(input(""))

# check the conditions and print accordingly
if (direction == "up"):
  print("I am painting in the upward direction!")
elif (direction == "down"):
  print("I am painting in the downward direction!")
elif (direction == "left"):
  print("I am painting in the left direction!")
else: 
  print("I am painting in the right direction!")