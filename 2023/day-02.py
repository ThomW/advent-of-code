test_values = [
'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
]

def partOne(data):

  limits = {
    'red': 12,
    'green': 13,
    'blue': 14
  }

  ret = 0

  for line in data:

    game_id = int(line.split(':')[0].split(' ')[1])
    games = line.split(':')[1].split(';')
    color_max = {'red': 0, 'green': 0, 'blue': 0}
    
    for game in games:
      cube_counts = game.split(',')
      for cube_count in cube_counts:
        count = int(cube_count.strip().split(' ')[0].strip())
        color = cube_count.strip().split(' ')[1].strip()
        if count > color_max[color]:
          color_max[color] = count
      
    is_valid = True
    for color, count in color_max.items():
      if count > limits[color]:
        is_valid = False
        break
    
    if is_valid:
      ret += game_id

  return ret

def partTwo(data):

  ret = 0

  for line in data:

    game_id = int(line.split(':')[0].split(' ')[1])
    games = line.split(':')[1].split(';')
    cubes_required = {'red': 0, 'green': 0, 'blue': 0}
    
    for game in games:
      cube_counts = game.split(',')
      for cube_count in cube_counts:
        count = int(cube_count.strip().split(' ')[0].strip())
        color = cube_count.strip().split(' ')[1].strip()
        if count > cubes_required[color]:
          cubes_required[color] = count
    
    ret += cubes_required['red'] * cubes_required['green'] * cubes_required['blue']
  
  return ret


with open ('day-02.txt', 'r') as f:
  values = f.readlines()

print('Problem 1 Test Value (Target 8): {}'.format(partOne(test_values)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Test Value (Target 2286): {}'.format(partTwo(test_values)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
