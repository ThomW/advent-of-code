import re

sample_data = [
  [0, 9, 5, 9]
, [8, 0, 0, 8]
, [9, 4, 3, 4]
, [2, 2, 2, 1]
, [7, 0, 7, 4]
, [6, 4, 2, 0]
, [0, 9, 2, 9]
, [3, 4, 1, 4]
, [0, 0, 8, 8]
, [5, 5, 8, 2]
]

# Constants to make it easier to find the elements in the data
x1 = 0
y1 = 1
x2 = 2
y2 = 3

# 
def output_grid(grid):
  for row in grid:
    for col in row:
      if col == 0:
        print('.', end='')
      else:
        print(f'{col}', end='')
    print('')

# Find the overlapping lines
def solve(data, print_grid = False, do_diagonals = False):

  # Find the max x and y values so we know how large to make the grid
  grid_x_size, grid_y_size = 0, 0
  for line in data:
    grid_x_size = max(grid_x_size, line[x1], line[x2])
    grid_y_size = max(grid_y_size, line[y1], line[y2])

  # Initialize the grid by filling it with zeroes
  grid = []
  for y in range(0, grid_y_size + 1):
    grid.append([0] * (grid_x_size + 1))

  # When dealing with grid, it's important to remember that the coordinate system is flipped
  # -- grid is made up of rows(y) of columns(x)

  # Loop through the coordinates and count the number of times each cell in the grid is touched
  for line in data:

    if line[x1] == line[x2]:
      for y in range(min(line[y1], line[y2]), max(line[y1], line[y2]) + 1):
        grid[y][line[x1]] += 1
        
    elif line[y1] == line[y2]:
      for x in range(min(line[x1], line[x2]), max(line[x1], line[x2]) + 1):
        grid[line[y1]][x] += 1

    # Part two requires that we deal with diagonals, in in this puzzle, they're all
    # 45 degree lines, so that makes this calculation simple since the X and Y coordinates
    # all move the same amount
    elif do_diagonals:
      num_points = max(line[x1], line[x2]) - min(line[x1], line[x2]) + 1
      x_dir = line[x1] > line[x2] and -1 or 1
      y_dir = line[y1] > line[y2] and -1 or 1
      for n in range(0, num_points):
        grid[line[y1] + n * y_dir][line[x1] + n * x_dir] += 1

  if print_grid:
    output_grid(grid)

  # count and return the overlaps, which is cells with a value higher than one
  overlaps = 0
  for row in grid:
    for col in row:
      if col > 1:
        overlaps += 1

  return overlaps

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
data = []
with open ('day-05.txt', 'r') as f:
  for str in f.readlines():
    m = re.match(r"(\d*),(\d*) -> (\d*),(\d*)", str.strip())
    data.append([int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))])

print('Problem 1 Sample Value (Target 5): {}'.format(solve(sample_data, print_grid = True)))
print('Problem 1 Solution: {}'.format(solve(data)))

print('Problem 2 Sample Value (Target 12): {}'.format(solve(sample_data, print_grid = True, do_diagonals = True)))
print('Problem 2 Solution: {}'.format(solve(data, do_diagonals=True)))
