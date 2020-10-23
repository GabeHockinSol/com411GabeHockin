#Introduction
print("what type of adventure do you want to go on?")
print("scary\n")
print("short\n")
print("safe\n")
print("long\n")

#Get players answer
answer = str(input())

# checks the answer and displays the message accordingly
if(answer == "scary") or (answer == "short"):
  print("Entering the dark forest!")
elif (answer == "safe") or (answer == "long"):
  print("Taking the safe route!")
else: print("Not sure which route to take.")