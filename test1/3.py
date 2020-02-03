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
from utils.webassign import array_from_shitstring_floats
from stats import frequency, relative_frequency, trimmed_mean

values = array_from_shitstring_floats('14.7	12.9	17.5	14.2	12.1	11.0	9.3	8.0')
print("Values: {}".format(values))


