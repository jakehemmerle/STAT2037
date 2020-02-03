"""
This file contains some default imports and commonly used functions so that you
don't have to write lots of code over and over for each problem.
"""

# CONFIG
PROJECT_ROOT = '..'  # relative location pointing to utils/ and stats.py

# REST OF FILE
import sys

# allows import of project files (idk how else to do this)
sys.path.insert(1, PROJECT_ROOT)
from utils.webassign import array_from_shitstring
from stats import frequency, relative_frequency

data = array_from_shitstring('1    1    2    3    0    1    3    2    0    5    3    3    1    3    2    4    7    0    2    3 0    4    2    1    3    1    1    3    4    1    2    3    2    2    8    4    5    1    3    1 5    0    2    3    2    1    0    6    4    2    1    6    0    3    3    3    7    1    2    3')  # put your data here
data.sort()
freq = frequency(data)
print("Data: {}".format(data))
print("frequency: {}".format(freq))
print("relative frequency: {}".format(relative_frequency(freq)))
