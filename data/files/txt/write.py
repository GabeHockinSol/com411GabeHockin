def search(file_name):
  print("Searching...", end = "")
  # empty lists ready to be stored
  sections = []
  books = []
  # Get the file path that was given from "Run" function
  with open(file_name) as file:
    for line in file:
      # check for "Section" and store it in the "section" # list else store eveything else in the "books" list
      if line.startswith("Section"):
        section_name = line.split(":")[1]
        sections.append(section_name.strip())
      else:
        books.append(line.strip())
  print("Done!")
  return (sections, books)


def save(file_name, data):
  print("Saving...", end = "")
  # re writing the text in the file path given to "search" the function
  with open(file_name, "w") as file:
    file.write(f"Sections: {data[0]} \n")
    file.write(f"Books: {data[1]} \n")
  print("Done!")


def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/books.txt", data)

run()