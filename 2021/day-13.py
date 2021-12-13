from time import time

example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

# Print dots to look like the puzzle examples for testing
def print_dots(dots, papersize):
  max_x, max_y = papersize
  print(f'{len(dots)} Dots:')
  for y in range(max_y + 1):
    for x in range(max_x + 1):
      if (x,y) in dots:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()

# Break up the textblobs into dots and folds
def process_input(data):
  dots = []
  folds = None
  for line in data.splitlines():
    if len(line) == 0:
      folds = []
    elif folds is None:
      x, y = line.split(',')
      dots.append((int(x), int(y)))
    else:
      axis, value = line[11:].split('=')
      folds.append((axis, int(value)))
  return dots, folds

# Finds the overall dimensions of the coordinate system
def get_max_xy(dots):
  max_x, max_y = 0, 0
  for x, y in dots:
    max_x = max(max_x, x)
    max_y = max(max_y, y)
  return max_x, max_y

# This does all the work involved in executing a fold
def do_fold(dots, paper_size, fold):
  fold_direction, fold_idx = fold
  paper_width, paper_height = paper_size
  
  new_dots = set() # Using a set to automatically dedupe dots once they're overlapping

  for x, y in dots:
    if fold_direction == 'y' and y > fold_idx:
      new_dots.add((x, paper_height - y))
    elif fold_direction == 'y' and y == fold_idx:
      pass # Dots on the fold get lost
    elif fold_direction == 'x' and x > fold_idx:
      new_dots.add((paper_width - x,  y))
    elif fold_direction == 'x' and x == fold_idx:
      pass # Dots on the fold get lost
    else:
      new_dots.add((x, y))

  # Update the dimensions of the paper
  if fold_direction == 'y':
    paper_height = paper_height - fold_idx - 1
  elif fold_direction == 'x':
    paper_width = paper_width - fold_idx - 1

  return new_dots, (paper_width, paper_height)

def partOne(data, max_folds = None, debug = False):
  dots, folds = process_input(data)

  # This is a lousy assumption, but they don't give us the paper size...
  paper_size = get_max_xy(dots)

  if debug:
    print_dots(dots, paper_size)

  for fold in folds:

    dots, paper_size = do_fold(dots, paper_size, fold)

    if debug:
      print_dots(dots, paper_size)

    # Handle fold limiter
    if max_folds is not None:
      max_folds -= 1
      if max_folds == 0:
        break

  return len(dots)

def partTwo(data):
  pass  

# Import the data file as just a text blob
values = ''
with open ('day-13.txt', 'r') as f:
  values = f.read()

# Do the complete example to test everything
print('Part 1 Full Example: {}'.format(partOne(example, debug = True)))

print('Part 1 Example 1 (Target 17): {}'.format(partOne(example, max_folds = 1, debug = True)))

print('Problem 1 Solution: {}'.format(partOne(values, max_folds = 1)))

#print('Part 2 Example 1 (Target ??): {}'.format(partTwo(example_1)))

#print('Problem 2 Solution: {}'.format(partTwo(values)))
