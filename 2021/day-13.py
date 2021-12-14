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
def print_dots(dots):

  max_x, max_y = 0, 0
  for x, y in dots:
    max_x = max(max_x, x)
    max_y = max(max_y, y)

  print(f'{len(dots)} Dots:')
  for y in range(max_y + 1):
    for x in range(max_x + 1):
      if (x,y) in dots:
        print('#', end='')
      else:
        print('.', end='')
    print()
  print()

# Break up the input into dots and folds
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

# This does all the work involved in executing a fold
def do_fold(dots, fold):
  fold_direction, fold_idx = fold
  
  new_dots = set() # Using a set to automatically dedupe dots once they're overlapping

  for x, y in dots:
    if fold_direction == 'y' and y > fold_idx:
      new_dots.add((x, fold_idx + fold_idx - y))
    elif fold_direction == 'y' and y == fold_idx:
      pass # Dots on the fold get lost
    elif fold_direction == 'x' and x > fold_idx:
      new_dots.add((fold_idx + fold_idx - x,  y))
    elif fold_direction == 'x' and x == fold_idx:
      pass # Dots on the fold get lost
    else:
      new_dots.add((x, y))

  return new_dots

def solve(data, max_folds = None, debug = False, print_resulting_dots=False):
  dots, folds = process_input(data)

  if debug:
    print_dots(dots)

  for fold in folds:
    dots = do_fold(dots, fold)

    if debug:
      print_dots(dots)

    # Handle fold limiter
    if max_folds is not None:
      max_folds -= 1
      if max_folds == 0:
        break

  if print_resulting_dots:
    print_dots(dots)

  return len(dots)

# Import the data file as just a text blob
values = ''
with open ('day-13.txt', 'r') as f:
  values = f.read()

# Do the complete example to test everything
print('Part 1 Full Example: {}'.format(solve(example, debug = True)))

print('Part 1 Example 1 (Target 17): {}'.format(solve(example, max_folds = 1, debug = True)))

print('Problem 1 Solution: {}'.format(solve(values, max_folds = 1)))

print('Problem 2 Solution:')
solve(values, print_resulting_dots=True)
