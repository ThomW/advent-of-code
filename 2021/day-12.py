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

  valid_paths = []
  queue = [['start']]
  while len(queue) > 0:
    path = queue.pop(0)
    for node in nodes[path[-1]]:
      if (node == 'end'):
        valid_paths.append(path + [node])
      elif node in path:
        if node.isupper():
          queue.append(path + [node])
      else:
        queue.append(path + [node])

  return len(valid_paths)

# Finds all the paths from start to end, allowing just one lowercase node to be visited twice
def partTwo(data):
  
  nodes = process_input(data)

  valid_paths = []
  queue = [['start']]
  while len(queue) > 0:
    print(len(queue)) # This helped me keep my sanity as the script took a while to run
    path = queue.pop(0)
    # print(path)
    for node in nodes[path[-1]]:
      if (node == 'end'):
        valid_paths.append(path + [node])
      elif node == 'start':
        pass
      elif node.isupper():
        queue.append(path + [node])
      elif node not in path:
        queue.append(path + [node])
      else:
        # Count the number of lowercase nodes in the path and make sure that we're not
        # going to cause more than one lowercase node to be visited twice
        lower_counts = {}
        for n in path:
          if n.islower():
            if n in lower_counts.keys():
              lower_counts[n] += 1
            else:
              lower_counts[n] = 1
        if not 2 in lower_counts.values():
          queue.append(path + [node])

  # Print the valid paths in a format that matched the examples
  #for vp in valid_paths:
  #  print(','.join(vp))

  return len(valid_paths)

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

print('Problem 2 Solution: {}'.format(partTwo(values)))
