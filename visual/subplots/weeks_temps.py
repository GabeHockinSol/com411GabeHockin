import matplotlib.pyplot as plt
import csv

def read_data():
  # open file
  with open('visual/subplots/temps.csv') as file:
    csv_reader = csv.reader(file)
    
    # store the data from "temps.csv"
    header = next(csv_reader)
    data = {'week1':[], 'week2':[]}

    for line in csv_reader:
      data['week1'].append(float(line[0].strip()))
      data['week2'].append(float(line[1].strip()))
  
  return data

def run():
  # grab the data stored from "Read_data"
  data = read_data()
  
  # put data into graphs
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data['week1'])), data['week1'])
  ax2.plot(range(len(data['week2'])), data['week2'])
  plt.show()

run()