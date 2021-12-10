sample_data = ['[({(<(())[]>[[{[]{<()<>>'
,'[(()[<>])]({[<{<<[]>>('
,'{([(<{}[<>[]}>{[]{[(<()>'
,'(((({<>}<{<{<>}{[]{[]{}'
,'[[<[([]))<([[{}[[()]]]'
,'[{[{({}]{}}([{[{{{}}([]'
,'{<[[]]>}<{[{[{[]{()[[[]'
,'[<(<(<(<{}))><([]([]()'
,'<{([([[(<>()){}]>(<<{{'
,'<{([{{}}[<[[[<>{}]]]>[]]']

def remove_pairs(line):
    while 1:
      last_line = line
      line = line.replace('()', '')
      line = line.replace('[]', '')
      line = line.replace('{}', '')
      line = line.replace('<>', '')
      if last_line == line:
        return line

def score_line(line):
  illegal_chars = {')': 3, ']': 57, '}': 1197, '>': 25137}
  for char in line:
    if char in illegal_chars.keys():
      return illegal_chars[char]
  return 0

"""
To calculate the syntax error score for a line, take the
first illegal character on the line and look it up in the
following table:

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.

Add up the value of each first-found illegal character.
"""
def partOne(data):

  # This obviously got refactored while doing part two since
  # it's used there...

  score = 0
  for line in data:
    score += score_line(remove_pairs(line))
  return score

# Find incomplete lines and calculate a score based on what it
# would take to complete the lines
# We really don't care about completing the strings -- just
# calculating the point values
def partTwo(data):

  all_scores = []

  for line in data:
    line = remove_pairs(line)

    # We only care about incomplete lines, so if a line's
    # score is 0, that means it's just incomplete
    if score_line(line) == 0:
      char_points = {'(': 1, '[': 2, '{': 3, '<': 4}
      for char in line[::-1]: # Read the string in reverse to correctly calculate score
        score = 5 * score + char_points[char]
      all_scores.append(score)

  # Return the middle value
  all_scores.sort()
  return all_scores[int(len(all_scores) * 0.5)]

# Import the data file into a list of lists of four elements reprenting x1,y1,x2,y2
values = []
with open ('day-10.txt', 'r') as f:
  for tmp in f.readlines():
    values.append(tmp.strip())

print('Problem 1 Sample Value (Target 26397): {}'.format(partOne(sample_data)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Sample Value (Target 288957): {}'.format(partTwo(sample_data)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
