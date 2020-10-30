def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please enter a direction:")
  direction_list = directions()

  for index in range(len(direction_list)):
    print("{}: {}".format(index, direction_list[index]))

# call the menu
def run():
  menu()

# Call the run function
run()