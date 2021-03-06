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
from stats import mean, median, trimmed_mean

psi_data = array_from_shitstring_floats('14.7	12.9	17.5	14.2	12.1	11.0	9.3	8.0')
print("PSI data: {}".format(psi_data))

print("Sample mean: {}".format(mean(psi_data)))
print("Sample median: {}".format(median(psi_data)))
print("Trimmed mean 12.5%: {}".format(trimmed_mean(psi_data, .125)))


