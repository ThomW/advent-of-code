
group_answers = []

def process_buffer(data):
  group = {}
  for line in data:
    for d in line:
      if d in group.keys():
        group[d] += 1
      else:
        group[d] = 1
  return group

buffer = []
with open ("day-06.txt", "r") as f:
  for line in [line.strip() for line in f]:
    # If we hit a blank line, process the accumulated buffer
    if len(line) == 0:
      group_answers.append({'answers': process_buffer(buffer), 'num_passengers': len(buffer)})
      buffer = []
    # Accumulate lines into buffer
    else:
      buffer.append(line)
  if len(buffer):
    group_answers.append({'answers': process_buffer(buffer), 'num_passengers': len(buffer)})

# Part one - count the number of unique numbers for each group and get the sum of all the counts
sum_of_counts = 0
for group in group_answers:
  sum_of_counts += len(group['answers'].keys())
print("Part One: Sum of all the counts = {}".format(sum_of_counts))

# Part two - we have to find the count of the letters that each group all answered yes
# and return the sum of those values
sum_of_agreements = 0
for group in group_answers:
  group_sum = 0
  for answer in group['answers'].keys():
    if group['answers'][answer] == group['num_passengers']:      
      group_sum += 1
  sum_of_agreements += group_sum

print("Part Two: Sum of all the agreements = {}".format(sum_of_agreements))

    