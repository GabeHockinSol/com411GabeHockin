from tech import Tech
class JetPack(Tech):
  def __init__(self):
    super().__init__()

  def __repr__(self):
    return "jetpack()"
  def activate():
    print("Jetpack on")

  def deactivate():
    print("Jetpack off")

if __name__ == "__main__":
  jetpack = JetPack()
  print(repr(jetpack))