test_data = """11111
19991
19191
19991
11111"""

sample_data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

class bcolors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'

# Converts the multi-line string into a 2D array
def listify_input(data):
  ret = []
  for line in data.splitlines():
    row = []
    for char in list(line):
      row.append(int(char))
    ret.append(row)
  return ret

# Print out the array with some style
def print_octopi(octopi, flashed = None):
  for y in range(len(octopi)):
    line = ''
    for x in range(len(octopi[y])):
      if flashed is not None and flashed[y][x]:
        print(f'{bcolors.WARNING}{octopi[y][x]}{bcolors.ENDC}', end='')
      else:
        print(f'{octopi[y][x]}', end='')
    print()
  print()

# This handles what constitutes as a step for the puzzle
# and it returns the array, the flashes array, and the number
# of flashes that occured in the step
def do_step(octopi):

  flashed = []
  num_flashes = 0

  # First, the energy level of each octopus increases by 1.
  # and build the flashed array to track whether an octopus
  # has already flashed
  for y in range(len(octopi)):
    flashed_row = []
    for x in range(len(octopi[y])):
      flashed_row.append(False)
      octopi[y][x] += 1
    flashed.append(flashed_row)

  # Then, any octopus with an energy level greater than 9 flashes.
  # This increases the energy level of all adjacent octopuses by 1,
  # including octopuses that are diagonally adjacent. If this causes
  # an octopus to have an energy level greater than 9, it also flashes.
  # This process continues as long as new octopuses keep having their
  # energy level increased beyond 9. (An octopus can only flash at
  # most once per step.)
  while True:
    new_flashes = 0
    for y in range(len(octopi)):
      for x in range(len(octopi[y])):
        # An octopus can only flash once, so only count the instant it's over 9
        if octopi[y][x] > 9 and not flashed[y][x]:
          octopi[y][x] = 0
          flashed[y][x] = True
          new_flashes += 1
          for flashy in [y - 1, y, y + 1]:
            for flashx in [x - 1, x, x + 1]:
              if flashy >= 0 and flashy < len(octopi) and flashx >= 0 and flashx < len(octopi[y]) and not flashed[flashy][flashx]:
                octopi[flashy][flashx] += 1
    
    if new_flashes == 0:
      break
    else:
      num_flashes += new_flashes

  return octopi, flashed, num_flashes

def partOne(data, num_steps):
  
  octopi = listify_input(data)

  total_flashes = 0

  for step in range(num_steps):
    print(f'Step {step + 1}:')
    octopi, flashed, num_flashes = do_step(octopi)
    print_octopi(octopi, flashed)

    # Accumulate flashes
    total_flashes += num_flashes

  return total_flashes

# Find the first step where all the octopi flash at once
def partTwo(data):

  octopi = listify_input(data)

  # This is the number of flashes we'd have if all the octopi flashed at once
  target_num_flashes = len(octopi) * len(octopi[0])

  step = 0
  while True:
    step += 1
    octopi, flashed, num_flashes = do_step(octopi)
    if num_flashes == target_num_flashes:
      return step

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
values = ''
with open ('day-11.txt', 'r') as f:
  values = f.read()

print('Problem 1 Test: {}'.format(partOne(test_data, 2)))

print('Problem 1 Sample Pt 1 Value (Target 204): {}'.format(partOne(sample_data, 10)))
print('Problem 1 Sample Pt 2 Value (Target 1656): {}'.format(partOne(sample_data, 100)))
print('Problem 1 Solution: {}'.format(partOne(values, 100)))

print('Problem 2 Sample Value (Target 195): {}'.format(partTwo(sample_data)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
