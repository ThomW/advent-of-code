sample_data = [3,4,3,1,2]

def solve(data, days):

  # Initialize fish_counts
  # Fish counts is a Dictionary where the key is the age of each fish
  # and the value is the count of the fish at that age
  fish_counts = [0] * 9
  for n in data:
    fish_counts[n] += 1
    
  # Process fish each day
  for day in range(0, days):

    # Shuffle all of the fish counts down one index
    fish_counts.append(fish_counts.pop(0))

    # The spawned fish live at 8, but we need to reset their parents from what was 0 -> 6
    fish_counts[6] += fish_counts[8]
    
    print(f"Day {day}: {sum(fish_counts)}")

  return sum(fish_counts)

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
values = []
with open ('day-06.txt', 'r') as f:
  str = f.readline()
  for s in str.split(','):
    values.append(int(s.strip()))

print('Problem 1 Sample Value (Target 26): {}'.format(solve(sample_data, 18)))
print('Problem 1 Sample Value (Target 5934): {}'.format(solve(sample_data, 80)))
print('Problem 1 Solution: {}'.format(solve(values, 80)))

print('Problem 2 Sample Value (Target 26984457539): {}'.format(solve(sample_data, 256)))
print('Problem 2 Solution: {}'.format(solve(values, 256)))
