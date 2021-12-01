test_values = [
199
, 200
, 208
, 210
, 200
, 207
, 240
, 269
, 260
, 263
]

def partOne(data):
  ret = 0
  last_value = None
  for n in data:
    if last_value != None and n > last_value:
      ret += 1
    last_value = n
  return ret

def partTwo(data):
  count_of_increases = 0
  if len(data) > 3:
    for n in range(3, len(data)):
      if data[n] + data[n-1] + data[n-2] > data[n-1] + data[n-2] + data[n-3]:
        count_of_increases += 1
  return count_of_increases

with open ('day-01.txt', 'r') as f:
  values = [int(i) for i in f.readlines()]

print('Problem 1 Test Value (Target 7): {}'.format(partOne(test_values)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Test Value (Target 5): {}'.format(partTwo(test_values)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
