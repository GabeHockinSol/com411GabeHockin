# prompts the user for how many drawings
drawingCount = int(input("How manu mountains should I draw?\n"))

# store a string of the mountain so that we can call it later
mountain = str ( "          __ \n"
                 "         /  \_ \n" 
                 "        /^    \ \n"
                 "       /  ^    \_ \n"
                 "     _/ ^ ^     ^\ \n"
                 "    /  ^     ^    \ \n" )

# tracks how many mountains have been drawn
count = int()
for count in range(0, drawingCount, 1):
  count += 1
  print(mountain)

# Completed text
if(count == drawingCount):
  print("Done!")