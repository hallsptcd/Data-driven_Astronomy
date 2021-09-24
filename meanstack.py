
#This mean_datasets function reads in a list of CSV files of equal shape and
#returns an array of the mean of each cell in the data files.

def mean_datasets(files):
  import numpy as np
  n = len(files)
  data = np.loadtxt(files[0], delimiter=',')
  for i in range(1,n):
    data += np.loadtxt(files[i], delimiter=',')
  return np.round(data / n, 1)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))
