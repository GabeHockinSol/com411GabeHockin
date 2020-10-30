# function for movement directions (dir)
def movements():
  dir = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return dir

# function to print to log
def run():
  print("Moving...")
  dir = movements()
  for count in range(0, len(dir), 2):
    print(f"{dir[count]} for {dir[count+1]} steps")

# call run function
run()