import matplotlib.pyplot as plt

def read_data(file_path):
  # collect data and store so that it can be called in "run"
  data = []
  with open(file_path) as file:
    for line in file:
      data.append(float(line.strip()))
  return data

def run():
  data = read_data("visual/subplots/temps.txt") #get the data file
  # put into graphs
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data)), data)
  ax2.bar(range(len(data)), data)
  plt.show()

run()