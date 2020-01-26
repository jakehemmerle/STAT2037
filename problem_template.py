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

data = array_from_shitstring('DATA_HERE')  # put your data here
data.sort()
print("Data: {}".format(data))
