with open ("day-03.txt", "r") as f:
  data = [line.rstrip() for line in f]

def tree_counter(step_x, step_y):
  x = 0
  y = 0

  tree_counter = 0

  while y < len(data):

    # Wrap X to make the map infinite horizontally  
    if x >= len(data[y]):
      x -= len(data[y])

    # Test for a tree
    if data[y][x] == '#':
      tree_counter += 1

    # Move to the next position
    x += step_x
    y += step_y

  return tree_counter

def part_two():
  
  product = 0

  # Walk the trees and display the counts
  for step in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
    count = tree_counter(step[0], step[1])
    print('Part Two - Trees hit {} {}: {}'.format(step[0], step[1], count))
    
    # Accumulate the products of the counts
    if product == 0:
      product = count
    else:
      product *= count

  print('Product of counts: {}'.format(product))  

print('Part One - Trees hit: {}'.format(tree_counter(3, 1)))
print('')
part_two()
