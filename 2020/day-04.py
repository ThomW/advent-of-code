import re

required_fields = {
   'byr': '^19[2-9][0-9]|200[0-2]$'
  ,'iyr': '^201[0-9]|2020$'
  ,'eyr': '^202[0-9]|2030$'
  ,'hgt': '^1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in$'
  ,'hcl': '^\#[0-9,a-f]{6}$'
  ,'ecl': '^amb|blu|brn|gry|grn|hzl|oth$'
  ,'pid': '^[0-9]{9}$'
}

valid_passport_field_count = 0 # Holds result for part one
valid_passport_value_count = 0 # Holds result for part two

# Converts the string containing all of the passport data into a dictionary
def parse_passport(str):
  passport = {}
  pairs = str.split(' ')
  fields = []
  for pair in pairs:
    if len(pair):
      kv = pair.split(':')
      passport[kv[0]] = kv[1]  
  return passport

# Returns True if all of the required fields are present
def validate_passport_fields(passport):
  for key in required_fields.keys():
    if not key in passport.keys():
      print('{} is missing {}'.format(passport, key))
      return False
  # If we get this far, all of the required fields are present
  return True

# Returns True if all of the fields validate
def validate_passport_values(passport):
  for key in required_fields.keys():
    if not re.search(required_fields[key], passport[key]):
      print('{} failed validation for {}: {}'.format(passport, key, required_fields[key]))
      return False
  return True

def process_buffer(buffer):
  global valid_passport_field_count, valid_passport_value_count

  # Convert the buffer into a map
  passport = parse_passport(buffer)

  # Validate the passport fields
  if validate_passport_fields(passport):
    valid_passport_field_count += 1

    # Validate the passport values after the fields are processed
    if validate_passport_values(passport):
      valid_passport_value_count += 1

buffer = ''
with open ("day-04.txt", "r") as f:
  for line in [line.strip() for line in f]:
    # If we hit a blank line, process the accumulated buffer
    if len(line) == 0:
      process_buffer(buffer)              
      buffer = ''
    # Accumulate lines into buffer
    else:
      buffer += line + ' '

if len(buffer):
  process_buffer(buffer)

print('Valid passports by fields: {}'.format(valid_passport_field_count))
print('Valid passports by fields and values: {}'.format(valid_passport_value_count))
