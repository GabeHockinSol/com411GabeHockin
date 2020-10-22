# prompts the user and stores the value either "soft" or "hard" into the bookCover varible
bookCover = input("What type of cover does the book have? soft or hard?: ")

# does a check to see if the book is soft
# if the book is soft then check another condition to see what type of bound it has
if (bookCover == "soft"):
  bound = input("Is the book perfect-bound? yes or no?: ")

  if(bound == "yes"):
    print("Soft cover, perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")
elif (bookCover == "hard"):
  print("Books with hard covers can be more expensive!")
