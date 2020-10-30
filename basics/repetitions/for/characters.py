markings = str(input("What strange markings do you see? \n"))

print ("Identifying...")
count = int(0)
for position in range(0, len(markings), 1):
    count += 1
    print("Index " + str(count) + ": " + markings[position])