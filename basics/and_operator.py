# Introduction
print("What did I hear? \n")
userHeared = input()
print("What did I see? \n")
userSaw = input()

#  if the user enters "grrr" for hear and enters "two red eyes" Then display
# "There is a scary creature. I should get out of here!"

if (userHeared == "grrr") and (userSaw == "two red eyes"):
  print("There is a scary creature. I should get out of here!")
else:
  print("I am a little scared but I will continue.")