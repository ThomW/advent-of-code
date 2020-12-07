import re

def find_bags_holding_target(tgt):
  # print('Searching for {}'.format(tgt))
  ret = set()
  for bag in bags:
    for child in bag['children']:
      if child == tgt:
        ret.add(bag['color'])
        break
  # If we found matches, dig deeper and find bags that can find the bags we just found
  if len(ret):
    addt_found = []
    for sub in ret:
      for found in find_bags_holding_target(sub):
        addt_found.append(found)
    for found in addt_found:
      ret.add(found)
  return ret

# Read all the data into content
with open ('day-07.txt', 'r') as f:
  content = f.readlines()

# Part One ================================================

# TESTING  - target is 4
'''
content = [
  'light red bags contain 1 bright white bag, 2 muted yellow bags.'
  ,'dark orange bags contain 3 bright white bags, 4 muted yellow bags.'
  ,'bright white bags contain 1 shiny gold bag.'
  ,'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.'
  ,'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.'
  ,'dark olive bags contain 3 faded blue bags, 4 dotted black bags.'
  ,'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.'
  ,'faded blue bags contain no other bags.'
  ,'dotted black bags contain no other bags.'
]
'''
bags = []
for line in content:
  match = re.search('^(.*) bags contain (.*)\.$', line)
  if match:
    parent_color = match.group(1)
    child_colors = []
    for str_child in match.group(2).split(','):
      match = re.search('^[ ]?(\d*) (.*) bags?.?$', str_child)
      if match:
        child_colors.append(match.group(2))
    bags.append({'color': parent_color, 'children': child_colors})

print('Part One: {}'.format(len(find_bags_holding_target('shiny gold'))))

# Part Two ================================================

# TESTING - target is 126
'''
content = [
  'shiny gold bags contain 2 dark red bags.'
  ,'dark red bags contain 2 dark orange bags.'
  ,'dark orange bags contain 2 dark yellow bags.'
  ,'dark yellow bags contain 2 dark green bags.'
  ,'dark green bags contain 2 dark blue bags.'
  ,'dark blue bags contain 2 dark violet bags.'
  ,'dark violet bags contain no other bags.'
]
'''

def count_child_bags(color):
  ret = 0
  for color, qty in bags[color].items():
    qty = int(qty)
    ret += qty
    ret += qty * count_child_bags(color)
  return ret

# Setup data structure 
# ['color': color, 'children': [{'color': qty, 'color2': qty, etc]]

bags = {}
for line in content:
  match = re.search('^(.*) bags contain (.*)\.$', line)
  if match:
    parent_color = match.group(1)
    child_data = {}
    for str_child in match.group(2).split(','):
      match = re.search('^[ ]?(\d*) (.*) bags?.?$', str_child)
      if match:
        child_data[match.group(2)] = match.group(1)
    bags[parent_color] = child_data

print('Part two: {}'.format(count_child_bags('shiny gold')))
