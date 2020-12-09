test_data = [
35
,20
,15
,25
,47
,40
,62
,55
,65
,95
,102
,117
,150
,182
,127
,219
,299
,277
,309
,576
]

def part_one(data, preamble_size):

  def test_pairs(data, tgt):
    for i in range(0, len(data)):
      for j in range(0, len(data)):
        if i == j:
          continue
        elif data[i] + data[j] == tgt:
          return True
    return False

  for idx in range(preamble_size, len(data)):
    tgt = data[idx]
    if not test_pairs(data[idx - preamble_size:idx], tgt):
      return tgt

def part_two(data, tgt):
  for idx in range(0, len(data)):
    for idx_add in range(1, len(data) - idx):
      current_set = data[idx:idx + idx_add]
      sum_set = sum(current_set)
      # print('{}: {}'.format(sum_set, current_set))
      if sum_set == tgt:
        return min(current_set) + max(current_set)      
      elif sum_set > tgt:
        break
  return None

# Read in file's contents as ints
with open ('day-09.txt', 'r') as f:
  numbers = [int(i) for i in f.readlines()]

# Part One
print ('Test Part One: {}'.format(part_one(test_data, 5)))
part_one_solution = part_one(numbers, 25)
print('Part One: {}'.format(part_one_solution))

# Part Two
print('Test Part Two: {}'.format(part_two(test_data, 127)))
print('Part Two: {}'.format(part_two(numbers, part_one_solution)))
