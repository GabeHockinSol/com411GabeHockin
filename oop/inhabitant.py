from abc import ABC
class Inhabitant(ABC):
  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0):
    #Instanced attributes
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY

  #Method to grow the inhabitant and + its age by 1
  def grow(self):
    self.age += 1

  def eat(self, amount):

    if (self.energy + amount > Inhabitant.MAX_ENERGY):
      self.energy = Inhabitant.MAX_ENERGY
    else:
      self.energy += amount

  def move (self, distance):
    potentialenergy = self.energy - distance
    if (potentialenergy < 0):
      self.energy = 0
      return self.energy - abs(potentialenergy)
    else:
      self.energy = potentialenergy
      return 0