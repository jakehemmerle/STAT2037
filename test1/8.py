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
from stats import combinations, permutations

cellular = 6
cordless = 6
corded = 6
sum = 18

print((combinations(12, 18) - combinations(12, 12)) / combinations(12, 18))
