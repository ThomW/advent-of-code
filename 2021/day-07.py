sample_data = [16,1,2,0,4,2,7,1,2,14]

def partOne(data):
  
  least_fuel_consumed = None

  for tgt in range(min(data), max(data)):
    fuel_consumed = 0
    for crab in data:
      fuel_consumed += abs(tgt - crab)
    if least_fuel_consumed is None or fuel_consumed < least_fuel_consumed:
      least_fuel_consumed = fuel_consumed
  
  return least_fuel_consumed

# Return the amount of fuel required to move to the optimal position
# using the new fuel rules in part two where each move's fuel costs
# are relative to the amount that needs to be moved
def partTwo(crabs):
  
  # Precalculate the amount of fuel required to move between positions
  # so that we're not calculating this for each move like a dummy
  fuel_usage_map = {}
  usage = 0
  for n in range(max(crabs) * 2):
    usage += n
    fuel_usage_map[n] = usage

  # Using the usage map we created, figure out which position is the
  # cheapest to get to.
  least_fuel_consumed = None
  for tgt in range(min(crabs), max(crabs)):
    fuel_consumed = 0
    for crab in crabs:
      fuel_consumed += fuel_usage_map[abs(tgt - crab)]
    if least_fuel_consumed is None or fuel_consumed < least_fuel_consumed:
      least_fuel_consumed = fuel_consumed

  return least_fuel_consumed

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
values = []
with open ('day-07.txt', 'r') as f:
  str = f.readline()
  for s in str.split(','):
    values.append(int(s.strip()))

print('Problem 1 Sample Value (Target 37): {}'.format(partOne(sample_data)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Sample Value (Target 168): {}'.format(partTwo(sample_data)))
print('Problem 2 Solution: {}'.format(partTwo(values)))

# Further optimization: 
#
# I could condense this down further by making a fuel map for part
# one with the correct fuel costs calculated, but in this case, it's
# not really necessary
#
# I'm guessing I could speed up all of this by instead of looping through
# each position, continuously look at the middle value and continuously 
# go to the index halfway between the shorter options, but with pre-calculating
# the fuel values, this is fast enough