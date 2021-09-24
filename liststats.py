
# This list_stats function takes a list and outputs the median and mean.

def list_stats(list):
  list.sort()
  l = len(list)
  s=sum(list)
  mean = s/l
  i = (l-1)//2
  if (l%2):
    median = list[i]
  else:
    median = (list[i] + list[i + 1])/2
  return(median, mean)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)

