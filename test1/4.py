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
from stats import get_range, variance, standard_deviation

o2_consumption = array_from_shitstring_floats('29.6	 49.4	 31.0	 28.4	 28.8	 25.4	 34.0	 29.8	 23.8	 30.1')
print("O2 Consumption: {}".format(o2_consumption))

print("Sample range: {}".format(get_range(o2_consumption)))
print("Sample variance: {}".format(variance(o2_consumption)))
print("Standard deviation: {}".format(standard_deviation(o2_consumption)))


