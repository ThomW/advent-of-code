test_values = [
 '00100'
,'11110'
,'10110'
,'10111'
,'10101'
,'01111'
,'00111'
,'11100'
,'10000'
,'11001'
,'00010'
,'01010'
]

# Converts binary map string to an int
def mapToValue(str):
  ret = 0
  for n in range(0, len(str)):
    pwr = len(str) - n - 1 # ew
    if str[n] == '1':
      ret += 2 ** pwr
  return ret

# Builds gamma and epsilon maps showing which value is most/least common in each column
def getMaps(data):
  # Fill ones with a variable number of columns
  ones = []
  for n in range(0, len(data[0])):
    ones.append(0)

  # Accumulate the number of ones for each column
  for bin in data:
    for n in range(0, len(bin)):
      if bin[n] == '1':
        ones[n] += 1
  
  # This is hokey, but it lets me see the pattern as it appears in the example
  gamma_map = ''
  epsilon_map = ''
  for n in range(0, len(ones)):
    # More than half of the values are ones, so it's part of gamma
    if ones[n] > len(data) * 0.5:
      gamma_map += '1'
      epsilon_map += '0'
    elif ones[n] < len(data) * 0.5:
      gamma_map += '0'
      epsilon_map += '1'
    # They're equal!
    else:
      gamma_map += '1'
      epsilon_map += '0'
  
  return gamma_map, epsilon_map

def partOne(data):

  gamma_map, epsilon_map = getMaps(data)

  gamma = mapToValue(gamma_map)
  epsilon = mapToValue(epsilon_map)

  # print('{} = {}'.format(gamma_map, gamma))
  # print('{} = {}'.format(epsilon_map, epsilon))

  return gamma * epsilon

def partTwoSolver(data, target_value):
  # clone data
  candidates = data[:]

  column = 0

  while len(candidates) > 1:
    gamma_map, epsilon_map = getMaps(candidates)
    
    if target_value == '1':
      column_target = gamma_map[column]
    else:
      column_target = epsilon_map[column]

    # print('column:' , column, 'target: ', target_value, 'column_tgt:', column_target)

    list = []
    for candidate in candidates:
      if candidate[column] == column_target:
        list.append(candidate)

    # print(list)
    candidates = list

    column += 1  
    
  return list[0]

def partTwo(data):

  o_map = partTwoSolver(data, '1')
  co_map = partTwoSolver(data, '0')

  # print(o_map, co_map)

  # Convert my goofy strings to int
  oxygen_generator = mapToValue(o_map)
  co2_scrubber = mapToValue(co_map)
  
  return oxygen_generator * co2_scrubber

with open ('day-03.txt', 'r') as f:
  values = [str.strip() for str in f.readlines()]

print('Problem 1 Test Value (Target 198): {}'.format(partOne(test_values)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Test Value (Target 230): {}'.format(partTwo(test_values)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
