example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

# Import the data file as just a text blob
puzzle_input = ''
with open ('day-14.txt', 'r') as f:
  puzzle_input = f.read()

def process_input(data):
	start, pair_data = data.split('\n\n')
	pairs = {}
	for line in pair_data.splitlines():
		tgt, insert = line.strip().split(' -> ')
		pairs[tgt] = insert
	return start, pairs

# Dumb brute_force implementation
def part_one(data, num_steps):

	start, pairs = process_input(data)

	for step in range(num_steps):
		# print(f'{step + 1}: {len(start)}', flush = (step % 10 == 0))
		next = ''
		for n in range(0, len(start) - 1):
			a = start[n]
			b = start[n + 1]
			if a + b in pairs:
				next += a + pairs[a + b]
			else:
				next += a
		next += start[-1]
		start = next
	
	# Build dictionary with char counts
	char_count = {}
	for char in next:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	
	# Find min/max values
	highest, lowest = -9999, 9999
	for v in char_count.values():
		highest = max(highest, v)
		lowest = min(lowest, v)

	return highest - lowest

print('Part 1 Example (Target 1588): {}'.format(part_one(example, 10)))
print('Part 1 Solution: {}'.format(part_one(puzzle_input, 10)))

# Definitely need to find a better solution. Maybe look back at day-06 (lanternfly)?
print('Part 2 Example (Target 2188189693529): {}'.format(part_one(example, 40)))
