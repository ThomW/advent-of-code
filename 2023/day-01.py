test_values = [
'1abc2',
'pqr3stu8vwx',
'a1b2c3d4e5f',
'treb7uchet',
]

test_values_2 = [
'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen',
]

def find_first_digit(str):
  for char in str:
    if char.isnumeric():
      return char
  return None

def partOne(data):
  values = []
  for line in data:
    first = find_first_digit(line)
    last = find_first_digit(line[::-1])
    values.append(int(first + last))
  return sum(values)

def get_jiggy(str, reverse=False):

  values = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  }

  for n in range(0, len(str)):
    if str[n].isnumeric():
      return str[n]
    elif not reverse:
      for key, value in values.items():
        if str[n:].startswith(key):
          return value
    else:
      for key, value in values.items():
        if str[n:].startswith(key[::-1]):
          return value

  return None

def partTwo(data):
  values = []
  for line in data:
    first = get_jiggy(line)
    last = get_jiggy(line[::-1], True)
    values.append(int(first + last))
  return sum(values)

with open ('day-01.txt', 'r') as f:
  values = f.readlines()

print('Problem 1 Test Value (Target 142): {}'.format(partOne(test_values)))
print('Problem 1 Solution: {}'.format(partOne(values)))

print('Problem 2 Test Value (Target 281): {}'.format(partTwo(test_values_2)))
print('Problem 2 Solution: {}'.format(partTwo(values)))
