def search(fileName):
  print("Searching...")
  with open(fileName) as file:
    for line in file.readlines():
      print(f"Looked in " + line.strip())
  print("...Done!")

def run():
  search("data/files/txt/locations.txt")

run()