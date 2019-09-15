'''
Jake Hemmerle

Open with:
exec(open('WebassignHelper.py').read())
'''

import collections

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

# Standard counting
def get_frequency(number_array):
  return collections.Counter(number_array)

# Frequency of item / total number of items
def get_relative_frequency(number_array):
  a = {}
  array_length = len(number_array)
  for number in number_array:
    a[number] = number_array[number] / array_length
  return a
