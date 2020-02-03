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
from stats import combinations, permutations

print("Number of permutations of 6 on 31: {}".format(combinations(6, 31)))

print("Combinations of 2 of each variety: {}".format(combinations(2, 11) * combinations(2, 7) * combinations(2, 13)))
print("Probability of 2 of each variety: {}".format(combinations(2, 11) * combinations(2, 7) * combinations(2, 13) / combinations(6, 31)))

first = combinations(6, 11) / combinations(6, 31)
second = combinations(6, 7) / combinations(6, 31)
third = combinations(6, 13) / combinations(6, 31)

print("Probability that all 6 are same variety: {}".format(sum([first, second, third])))
