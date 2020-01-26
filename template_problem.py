"""
This file contains some default imports and commonly used functions so that you
don't have to write lots of code over and over for each problem.
"""
import sys

# allows import of project files (idk how else to do this)
project_root = '..'     # relative location pointing to utils/ and stats.py, change to '.' if in root folder
sys.path.insert(1, project_root)
from utils.webassign import array_from_shitstring

data = array_from_shitstring('DATA_HERE')        # put your data here
print("Data: {}".format(data))

