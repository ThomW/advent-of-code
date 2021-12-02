test_values = [
  'forward 5'
, 'down 5'
, 'forward 8'
, 'up 3'
, 'down 8'
, 'forward 2'
]

def partOne(data):
  horiz = depth = 0
  
  for str in data:
    dir, x = str.split()
    x = int(x)

    if dir == 'forward':
      horiz += x
    elif dir == 'down':
      depth += x
    elif dir == 'up':
      depth -= x

  return horiz * depth

def partTwo(data):
  horiz = depth = aim = 0
  
  for str in data:
    dir, x = str.split()
    x = int(x)
  
    if dir == 'forward':
      horiz += x
      depth += aim * x
    elif dir == 'down':
      aim += x
    elif dir == 'up':
      aim -= x

  return horiz * depth

with open ('day-02.txt', 'r') as f:
  values = [str for str in f.readlines()]

print('Problem 1 Test Value (Target 150): {}'.format(partOne(test_values)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Test Value (Target 900): {}'.format(partTwo(test_values)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
