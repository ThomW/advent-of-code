from typing import DefaultDict

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

# Brute force collapses when things get too complicated, so this is
# a smarter approach to the problem
def part_two(data, steps):
	start, rules = process_input(data)

	print()
	print(start)

	# Initialize letter counter
	letters = DefaultDict(int)
	for char in start:
		letters[char] += 1

	# Convert start string into a map where key is letter combo, value is frequency
	pairs = DefaultDict(int)
	for n in range(0, len(start) - 1):
		pairs[start[n:n+2]] = 1

	# Loop through steps incrementing counters for matching pairs
	for step in range(0, steps):
		new_pairs = DefaultDict(int)
		for pair, frequency in pairs.items():

			# Follow rules to inject new values in the middle of pairs
			new_pairs[pair[0] + rules[pair]] += frequency
			new_pairs[rules[pair] + pair[1]] += frequency

			# Keep track of the new letters introduced into the overall string
			letters[rules[pair]] += frequency

		pairs = new_pairs

	return max(letters.values()) - min(letters.values())

# This is a rewrite of part_two that I wrote from memory using what
# I learned. 
def part_three(input, steps):

	start, rules = process_input(input)

	pairs = DefaultDict(int)
	for n in range(0, len(start) - 1):
		pairs[start[n:n+2]] = 1

	letters = DefaultDict(int)
	for char in start:
		letters[char] += 1

	for n in range(0, steps):
		new_pairs = DefaultDict(int)
		for pair, frequency in pairs.items():
			rule = rules[pair]
			new_pairs[pair[0] + rule] += frequency
			new_pairs[rule + pair[1]] += frequency
			letters[rule] += frequency
		pairs = new_pairs

	return max(letters.values()) - min(letters.values())

	# This looks just like my previous part_two and the 
	# values are the same, so I retained something ... haha

print('Part 1 Example (Target 1588): {}'.format(part_three(example, 10)))
print('Part 1 Solution: {}'.format(part_three(puzzle_input, 10)))

# Definitely need to find a better solution. Maybe look back at day-06 (lanternfly)?
print('Part 2 Example (Target 2188189693529): {}'.format(part_three(example, 40)))
print('Part 2 Solution: {}'.format(part_three(puzzle_input, 40)))
