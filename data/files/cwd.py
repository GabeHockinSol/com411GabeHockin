def cwd():
  # Get the path and store it
  import os
  path = os.getcwd()
  # display message and the path
  print("The current working directory is " + str(path))
  print("The directory contains the following:")
  for file in os.listdir(path):
    print(file)


# call the function
cwd()
