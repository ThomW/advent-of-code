
# Read all the data
with open ('day-08.txt', 'r') as f:
  instructions = f.readlines()

REASON_INFINITE_LOOP = 'infinite loop'
REASON_PROGRAM_FINISHED = 'program finished'

# Runs a program and will stop once it hits an infinite loop
def run_program(instructions):
  used_indexes = set()
  accumulator_value = 0
  idx = 0
  while idx not in used_indexes:
    used_indexes.add(idx)
    cmd = instructions[idx][0:3]
    val = int(instructions[idx][4:])
    if cmd == 'nop':
      idx += 1
    elif cmd == 'acc':
      accumulator_value += val
      idx += 1 
    elif cmd == 'jmp':
      idx += val
    # End program if it hits the final instruction
    if idx == len(instructions):
      return REASON_PROGRAM_FINISHED, accumulator_value
  
    # Keep idx in the bounds of the list elements
    idx = idx % len(instructions)  
  
  # Program hit an infinite loop
  return REASON_INFINITE_LOOP, accumulator_value

"""
# Part one testing data
instructions = [
   'nop +0'
  ,'acc +1'
  ,'jmp +4'
  ,'acc +3'
  ,'jmp -3'
  ,'acc -99'
  ,'acc +1'
  ,'jmp -4'
  ,'acc +6'
]
"""

reason, value = run_program(instructions)
print("Part One: accumulator_value: {}".format(value))  

"""
# Part two testing data
instructions = [
  'nop +0'
  ,'acc +1'
  ,'jmp +4'
  ,'acc +3'
  ,'jmp -3'
  ,'acc -99'
  ,'acc +1'
  ,'jmp -4'
  ,'acc +6'
]
"""

# Part two - each run, change one NOP to JMP or vice versa until the program exits correctly
idx = 0
while idx < len(instructions):
  tmp = instructions.copy()
  if tmp[idx][0:3] == 'jmp':
    tmp[idx] = tmp[idx].replace('jmp', 'nop')
  elif tmp[idx][0:3] == 'nop':
    tmp[idx] = tmp[idx].replace('nop', 'jmp')
  reason, value = run_program(tmp)
  if reason == REASON_PROGRAM_FINISHED:
    print('Part Two: accumulator_value: {}'.format(value))
    break
  else:
    idx += 1
