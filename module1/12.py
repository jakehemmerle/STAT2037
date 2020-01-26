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
from stats import variance, standard_deviation

data = array_from_shitstring("85  	105  	130  	160  	180  	195  	134  	145  	214  	105  	145  151  	153  	135  	87  	99  	94  	119  	129")  # put your data here
data.sort()
print("Oxidation induction time (min): {}".format(data))

data_variance = variance(data)
data_standard_deviation = standard_deviation(data)
print("Sample variance: {}".format(data_variance))
print("Standard deviation: {}".format(data_standard_deviation))

data_to_hours = [value / 60 for value in data]
data_variance_in_hours = variance(data_to_hours)
standard_deviation_in_hours = standard_deviation(data_to_hours)
print("Sample variance (hrs): {}".format(data_variance_in_hours))
print("Standard deviation (hrs): {}".format(standard_deviation_in_hours))


