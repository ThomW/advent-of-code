sample_data = [
 list('2199943210')
,list('3987894921')
,list('9856789892')
,list('8767896789')
,list('9899965678')]

def getValue(data, x, y):
  # Values out of range return 1000, which will help find
  # low points
  if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
    return 1000
  else:
    return int(data[y][x])

# Find all of the low points on your heightmap.
# What is the sum of the risk levels of all low points on your heightmap?
def partOne(data):
  low_points = []
  for x in range(len(data[0])):
    for y in range(len(data)):
      v = getValue(data, x, y)
      if v < getValue(data, x, y-1) \
          and v < getValue(data, x + 1, y) \
          and v < getValue(data, x, y + 1) \
          and v < getValue(data, x - 1, y):
          low_points.append(v)
  
  return sum(low_points) + len(low_points)

# From a point, find the bounds of the basin
# When a valid point is accounted for, it's filled
# with a 9 so it's not counted again.
def defineBasin(data, x, y):
  basin = []
  v = getValue(data, x, y)
  if v < 9:
    basin.append(v)
    data[y][x] = 9
    for xn, yn in [[-1,0],[1,0],[0,-1],[0,1]]:
      data, b = defineBasin(data, x + xn, y + yn)
      if len(b):
        basin += b
  return data, basin

# Find the three largest basins and multiply their sizes together.
def partTwo(data):

  # Clone data into map
  map = data[:]

  basins = []
  for x in range(len(map[0])):
    for y in range(len(map)):
      map, basin = defineBasin(map, x, y)
      if len(basin):
        basins.append(basin)
  
  # Find the sizes of the three largest basins and multiply them together
  sizes = []
  for basin in basins:
    sizes.append(len(basin))

  sizes.sort(reverse=True)

  total = 1
  for n in range(0, 3):
    total *= sizes[n]

  return total

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
values = []
with open ('day-09.txt', 'r') as f:
  for tmp in f.readlines():
    values.append(list(tmp.strip()))

print('Problem 1 Sample Value (Target 15): {}'.format(partOne(sample_data)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Sample Value (Target 1134): {}'.format(partTwo(sample_data)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
