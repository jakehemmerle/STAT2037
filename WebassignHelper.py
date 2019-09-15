'''
Jake Hemmerle

Open with:
exec(open('WebassignHelper.py').read())
'''

import collections
import math

# Paste those red numbers from Webassign in a file, call this function with filename.
# Returns array with those numbers.
# data = array_from_multiline_shitfile('shitfile.txt')
def array_from_multiline_shitfile(filename):
  shitfile = open(filename, 'r')
  shitstring = shitfile.read()
  string = shitstring.strip()
  string_array = string.split()
  number_array = []
  for number in string_array:
    number_array.append(float(number))
  number_array.sort()

  return number_array

# Standard counting ()
def get_frequency(number_array):
  return collections.Counter(number_array)

# Get total samples from a number_array ADT
def get_total_samples(number_array):
  total_samples = 0
  for item in number_array:
    total_samples += number_array[item]
  return total_samples

# Frequency of item / total number of items (in a number_array ADT)
def get_relative_frequency(number_array):
  total_samples = get_total_samples(number_array)
  print("Total samples:  %d" % total_samples)

  rel_freq = {}
  array_length = len(number_array)
  for number in number_array:
    rel_freq[number] = number_array[number] / total_samples
  return rel_freq

# sum of values / total values
def get_mean(array):
  sum = 0
  for value in array:
    sum += value
  return sum / len(array)

# get middle number
def get_median(array):
  '''
  get the middle number

  >>> get_median([2, 4, 6, 8, 10])
  6.0

  >>> get_median([2, 5, 7, 8, 9, 12, 13, 23, 65])
  9.0

  >>> get_median([2, 4, 6, 8, 10, 12])
  7.0
  '''

  halfway_point = math.floor(len(array) / 2)
  if (len(array) % 2 == 0):
    return float( (array[halfway_point - 1] + array[halfway_point]) / 2 )
  else:
    return float( array[halfway_point] )
  
# subtract largest from smallest number
def get_range(array):
  if (len(array) <=1):
    print("Error: array needs to have length of at least 2")
  return array[len(array)-1] - array[0]
