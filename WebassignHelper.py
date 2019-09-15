'''
Jake Hemmerle

Open with:
exec(open('WebassignHelper.py').read())
'''

# Paste those red numbers from Webassign in a file, call this function with filename.
# Returns array with those numbers.
def array_from_multiline_shitfile(filename):
  shitfile = open(filename, 'r')
  shitstring = shitfile.read()
  string = shitstring.strip()
  string_array = string.split()
  number_array = []
  for number in string_array:
    number_array.append(float(number))

  return number_array
