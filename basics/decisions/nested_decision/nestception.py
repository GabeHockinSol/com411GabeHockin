print("Where should I look \n")
print("in the bedroom? (press 1) \n")
print("in the bathroom? (press 2)\n")
print("in the lab? (press 3)\n")
decision = input()

# Decisions for bedroom
if(decision == "1"):
  print("Where in the bedroom should I look?\n")
  print("under the bed? (press 1)\n")
  print("in the cupboard? (press 2)\n")
  decision = input()
  if(decision == "1"):
    print("Found some shoes but no battery.\n")
    print("Better luck next time.\n")
  elif(decision == "2"):
    print("Found some mess but no battery.\n")
    print("Better luck next time.\n")

# Decisions for bathroom
if(decision == "2"):
  print("Where in the bathroom should I look?\n")
  print("in the bathtub? (press 1)\n")
  print("in the cupboard? (press 2)\n")
  decision = input()
  if(decision == "1"):
    print("Found a rubber duck but no battery.\n")
    print("Better luck next time.\n")
  elif(decision == "2"):
    print("Found a toothbrush but no battery.\n")
    print("Better luck next time.\n")

# Decisions for lab
if(decision == "3"):
  print("Where in the lab should I look?\n")
  print("on the table? (press 1)\n")
  print("in the cupboard? (press 2)\n")
  decision = input()
  if(decision == "1"):
    print("Yes! I found my battery!\n")
  elif(decision == "2"):
    print("Found some chemicals but no battery.\n")
    print("Better luck next time.\n")
