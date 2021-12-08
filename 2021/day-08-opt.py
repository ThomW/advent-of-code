# I realized I should have used sets for this thing
# to streamline my comparisons in part two. Instead of
# rolling list_in_list, I should have just been using
# issubset(), and calculating the five_tells() can be
# reduced down to a difference()

sample_data = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'
,'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc'
,'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg'
,'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb'
,'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea'
,'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb'
,'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe'
,'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef'
,'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb'
,'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']

# In the output values, how many times do digits 1, 4, 7, or 8 appear?
def partOne(data):
  counter = 0
  for line in data:
    output_values = line.split('|')[1]
    for pattern in output_values.split(' '):
      if len(pattern) in [2, 4, 3, 7]:
        counter += 1
  return counter

# Decode the output values from the pattens and output the total sum
# of all the decoded outputs
def partTwo(data):
  total = 0

  # Build the decoder
  decoder = {}
  for line in data:
    signal_patterns, output_values = line.split('|')

    # These are the ones that are obvious based on the
    # number of segments that are activated
    for pattern in signal_patterns.split(' '):
      pattern = set(list(pattern))
      if len(pattern) == 2:
        decoder[1] = pattern
      elif len(pattern) == 4:
        decoder[4] = pattern
      elif len(pattern) == 3:
        decoder[7] = pattern
      elif len(pattern) == 7:
        decoder[8] = pattern

    # Determine the rest of the decodings using the patterns above
    for pattern in signal_patterns.split(' '):
      pattern = set(list(pattern))
      if len(pattern) == 6:
        if decoder[4].issubset(pattern):
          decoder[9] = pattern
        elif decoder[1].issubset(pattern):
          decoder[0] = pattern
        else:
          decoder[6] = pattern
      elif len(pattern) == 5:
        if decoder[1].issubset(pattern):
          decoder[3] = pattern
        # Telling between 2 and 5 is tricky.
        # 5 is a five-digit pattern that matches the
        # parts of 4 that aren't in 1
        elif decoder[4].difference(decoder[1]).issubset(pattern):
          decoder[5] = pattern
        else:
          decoder[2] = pattern

    # Now use the decoder to decode the output values
    value = 0
    for output_value_code in output_values.split(' '):
      output_value_code = set(list(output_value_code))
      for decoded_value, code in decoder.items():
        if output_value_code == code:
          value = value * 10 + decoded_value
    
    # print(f'{output_values}: {value}')

    total += value

  return total

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
values = []
with open ('day-08.txt', 'r') as f:
  for tmp in f.readlines():
    values.append(tmp.strip())

print('Problem 1 Sample Value (Target 26): {}'.format(partOne(sample_data)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Sample Value (Target 61229): {}'.format(partTwo(sample_data)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
