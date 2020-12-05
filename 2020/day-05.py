import math

boarding_passes = []

def split_range(min, max, char):
  range = max - min + 1
  if char in ['F', 'L']:
    max -= round(range / 2)
  elif char in ['B', 'R']:
    min += math.floor(range / 2)
  return min, max

def splitter(str, min, max):
  for char in str:
    min, max = split_range(min, max, char)
    print('{} {} {}'.format(char, min, max))
  if str[-1] in ['F','L']:
    return min
  elif str[-1] in ['B','R']:
    return max

def process_data(data):
  print('row')
  row = splitter(line[0:7], 0, 127)
  print('seat')
  seat = splitter(line[7:10], 0, 7)
  # print('{}: row {}, column {}, seat ID {}'.format(line, row, seat, (row * 8 + seat)))
  return {
    'row': row
    ,'seat': seat
    ,'seat_id': row * 8 + seat
  }

# test data
# process_data("""FBFBBFFRLR: row 44, column 5, seat ID 357.
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.""".splitlines())

max_seat_id = 0

seat_ids = []

with open ("day-05.txt", "r") as f:
  for line in [line.strip() for line in f]:
    seat_ids.append(process_data(line)['seat_id'])

# Part one
print 'Part One: Max Seat ID: {}'.format(max(seat_ids))

# Part two
seat_ids.sort()
for x in range(int(min(seat_ids)), int(max(seat_ids))):
  if not x in seat_ids:
    print('Part Two: My Seat ID: {}').format(x)
