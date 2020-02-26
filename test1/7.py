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

forty = 4
sixty = 6
seventy_five = 5
total_bulbs = sum([forty, sixty, seventy_five])
total_bulb_combinations_of_3 = combinations(3, total_bulbs)

# THIS IS WORNG
prob_at_least_two_bulbs_are_75 = combinations(2, seventy_five) * combinations(1, total_bulbs - 2) / total_bulb_combinations_of_3
prob_all_3_are_75 = combinations(3, seventy_five) / total_bulb_combinations_of_3
print("Probability of exactly two of 3 being 75: {}".format(prob_at_least_two_bulbs_are_75 - prob_all_3_are_75))

num_all_3_are_40 = combinations(3, forty)
num_all_3_are_60 = combinations(3, sixty)
num_all_3_are_75 = combinations(3, seventy_five)
prob_of_all_same_rating = sum([num_all_3_are_40, num_all_3_are_60, num_all_3_are_75]) / total_bulb_combinations_of_3

print("All 3 are same: {}".format(prob_of_all_same_rating))

print(sum([combinations(1, forty), combinations(1, sixty), combinations(1, seventy_five)]) / total_bulb_combinations_of_3)

print(combinations(5, forty + sixty) / combinations(6, total_bulbs))




