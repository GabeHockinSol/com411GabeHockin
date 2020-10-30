def crossed_bridge(steps):
    # Display each step 
    for step in range(steps):
        print("Crossed step.") 

    # Display message
    if (steps > 5):
        print("The bridge is collapsing!")
    else: 
        print("We must keep going!")

# prompt the player
user = int(input("How many steps to cross the bridge? \n"))
crossed_bridge(user)