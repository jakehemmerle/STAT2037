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

forty = 9
sixty = 5
seventy_five = 6
total_bulbs = sum([forty, sixty, seventy_five])
total_bulb_combinations = combinations(1, total_bulbs)

# THIS IS WORNG
event_second_is_75 = combinations(1, sixty + forty) / combinations(1, total_bulbs)
probability_first_two_above_75 = event_second_is_75 / total_bulb_combinations
print("Probability first two are above 75: {}".format(probability_first_two_above_75))




