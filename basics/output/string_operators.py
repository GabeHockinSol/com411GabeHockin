print("Please enter the number of lives.")
lives = int(input())
print("Please enter the energy level.")
energy = int(input())
print("Please enter the shield level.")
shield = int(input())
print("Health has been set.")

livesChar = ("♥")
energyChar = ("♦")
shieldChar = ("♠")

print("Lives:    " +livesChar * lives)
print("Energy:   " +energyChar * lives)
print("Shield:   " +shieldChar * lives)