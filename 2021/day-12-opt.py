from time import time

example_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

example_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

example_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

# Converts the multi-line string input into a list of dictionaries that list
# their child nodes
def process_input(data):
  ret = {}
  for line in data.splitlines():
    node_a, node_b = line.split('-')
    if not node_a in ret.keys():
      ret[node_a] = [node_b]
    else:
      ret[node_a].append(node_b)
    if not node_b in ret.keys():
      ret[node_b] = [node_a]
    else:
      ret[node_b].append(node_a)
  return ret

# Finds all the paths from start to end, not allowing lowercase nodes to be visited more than once
def partOne(data):

  nodes = process_input(data)

  # Take advantage of Python wanting to pass this guy by reference
  valid_paths = []
  find_routes(nodes, ['start'], valid_paths)

  return len(valid_paths)

# Finds all the paths from start to end, allowing just one lowercase node to be visited twice
def partTwo(data):

  nodes = process_input(data)

  valid_paths = []
  find_routes(nodes, ['start'], valid_paths, True)

  return len(valid_paths)

def find_routes(nodes, path, all_routes, allow_second_cave_visit = False):
  for node in nodes[path[-1]]:
    if node == 'end':
      all_routes.append(path + [node])
    elif node == 'start':
      pass # Never re-enter start
    elif node.isupper() or node not in path:
      find_routes(nodes, path + [node], all_routes, allow_second_cave_visit=allow_second_cave_visit)
    elif allow_second_cave_visit:
      find_routes(nodes, path + [node], all_routes, allow_second_cave_visit=False)

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
values = ''
with open ('day-12.txt', 'r') as f:
  values = f.read()

print('Part 1 Example 1 (Target 10): {}'.format(partOne(example_1)))
print('Part 1 Example 2 (Target 19): {}'.format(partOne(example_2)))
print('Part 1 Example 3 (Target 226): {}'.format(partOne(example_3)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Part 2 Example 1 (Target 36): {}'.format(partTwo(example_1)))
print('Part 2 Example 2 (Target 103): {}'.format(partTwo(example_2)))
print('Part 2 Example 3 (Target 3509): {}'.format(partTwo(example_3)))

start = time()
print('Problem 2 Solution: {}'.format(partTwo(values)))
end = time()
print(f'It took {end - start} seconds!')
