# Test data to check that my solver is working in the expected directions
#test_diagtlbr = [50,14,16,23,6,7]
#test_diagbltr = [50,14,11,7,17,22]
test_col = [50,13,2,9,10,12]
test_row = [50,5,17,13,18,9]

sample_called = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

sample_boards = [
  [
     [22, 13, 17, 11,  0]
    ,[8,  2, 23,  4, 24]
    ,[21,  9, 14, 16,  7]
    ,[6, 10,  3, 18,  5]
    ,[1, 12, 20, 15, 19]
  ],
  [
     [3, 15,  0,  2, 22]
    ,[9, 18, 13, 17,  5]
    ,[19,  8,  7, 25, 23]
    ,[20, 11, 10, 24,  4]
    ,[14, 21, 16, 12,  6]
  ],
  [
     [14, 21, 17, 24,  4]
    ,[10, 16, 15,  9, 19]
    ,[18,  8, 23, 26, 20]
    ,[22, 11, 13,  6,  5]
    ,[2,  0, 12,  3,  7]
  ]
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# I originally wasn't doing this, but had to when I finally realized that my original column solver wasn't working ... oops
def print_board(board, called):
  for row in board:
    for col in row:
      str = ' {}'.format(col)[-2:]
      if col in called:
        print(f"{bcolors.WARNING}{str}{bcolors.ENDC} ", end='')
      else:
        print(f"{str} ", end='')
    print("")

# Returns list of matching values if found
def check_board(called, board):

  # I dread looking at other peoples' solutions because I know mine is lousy. 
  # I'm sure there's some cool matrix math you could do to get a real answer.

  # What stupid bingo doesn't allow for diagonals???
  '''
  if board[0][0] in called and board[1][1] in called and board[2][2] in called and board[3][3] in called and board [4][4] in called:
    return [board[0][0], board[1][1], board[2][2], board[3][3], board [4][4]]
  if board[0][4] in called and board[1][3] in called and board[2][2] in called and board[3][1] in called and board [4][0] in called:
    return [board[0][4], board[1][3], board[2][2], board[3][1], board [4][0]]
  '''

  for x in range(0,5):
    if board[x][0] in called and board[x][1] in called and board[x][2] in called and board[x][3] in called and board[x][4] in called:
      return [board[x][0], board[x][1], board[x][2], board[x][3], board[x][4]]
    if board[0][x] in called and  board[1][x] in called and  board[2][x] in called and  board[3][x] in called and  board[4][x] in called:
      return [board[0][x], board[1][x], board[2][x], board[3][x], board[4][x]]
  return None

# Returns the sum of the unmarked numbers times the value of the winning ball
# which is the value asked for by both parts of today's puzzle
def getResult(board, called, ball):
  sum_of_unmarked_numbers = 0
  for row in board:
    for col in row:
      if col not in called:
        sum_of_unmarked_numbers += col

  print('sum_of_unmarked_numbers', sum_of_unmarked_numbers)

  # Return the product of the last called ball times the sum of all unmarked numbers
  return ball * sum_of_unmarked_numbers

# Find the first board to win
def partOne(queue, boards):
  
  called = []
  for ball in queue:

    print('ball: {}'.format(ball))

    called.append(ball)

    # Check the boards against the now-called balls
    for board in boards:
      match = check_board(called, board)
      if match is not None:

        print('Match:', match)

        print_board(board, called)

        return getResult(board, called, ball)        

# Figure out which card will win last, and return the last ball called and the sum of unmarked numbers
def partTwo(queue, boards):
  
  called = []
  for ball in queue:

    print('ball: {}'.format(ball))
    called.append(ball)

    # Check the boards against the now-called balls
    for board in boards:
      match = check_board(called, board)
      # Found a match with the current board ... 
      if match is not None:
        # If this is the last board, we found the winning number
        if len(boards) == 1:
          print_board(boards[0], called)
          return getResult(boards[0], called, ball)
        else:
          boards.remove(board)

  return None

with open ('day-04.txt', 'r') as f:
  called = [int(str) for str in f.readline().strip().split(',')]

  boards = []
  line = f.readline() # skip blank
  done = False
  while not done:
    board = []
    for n in range(0, 5):
      line = f.readline()
      if line == '':
        done = True
      else:
        line = line.replace('  ', ' ') # Hacky - could be regex
        # print('line: ', line)
        strings = line.strip().split(' ')
        # print('strings:', strings)
        row = []
        for n in strings:
          row.append(int(n))
          # print('row', row)
        board.append(row)
        # print(board)

    if len(board):    
      boards.append(board)
    
    line = f.readline() # Skip blank

# Test
# print('Test diagonal TL -> BR: {}'.format(partOne(test_diagtlbr, sample_boards)))
# print('Test diagonal BL -> TR: {}'.format(partOne(test_diagbltr, sample_boards)))
print('Test col: {}'.format(partOne(test_col, sample_boards)))
print('Test row: {}'.format(partOne(test_row, sample_boards)))

print('Problem 1 Sample Value (Target 4512): {}'.format(partOne(sample_called, sample_boards)))
print('Problem 1 Solution: {}'.format(partOne(called, boards)))

print('Problem 2 Sample Value (Target 1924): {}'.format(partTwo(sample_called, sample_boards)))
print('Problem 2 Solution: {}'.format(partTwo(called, boards)))
