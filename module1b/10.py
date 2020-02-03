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

thirteen_watt = 8
eighteen_watt = 9
twenty_three_watt = 7
total_bulbs = sum([thirteen_watt, eighteen_watt, twenty_three_watt])
total_combinations_of_3 = combinations(3, total_bulbs)

num_two_of_three_are_twenty_three = combinations(2, twenty_three_watt) * combinations(1, thirteen_watt + eighteen_watt)
prob_exactly_two_are_twenty_three = num_two_of_three_are_twenty_three / total_combinations_of_3
print("Probability that exactly two are rated 23-watt: {}".format(prob_exactly_two_are_twenty_three))

num_all_are_13 = combinations(3, thirteen_watt)
num_all_are_18 = combinations(3, eighteen_watt)
num_all_are_23 = combinations(3, twenty_three_watt)
prob_all_3_are_same = sum([num_all_are_13, num_all_are_18, num_all_are_23]) / total_combinations_of_3
print("probability that all three are same: {}".format(prob_all_3_are_same))

prob_one_bulb_of_each_type = combinations(1, thirteen_watt) * combinations(1, eighteen_watt) * combinations(1, twenty_three_watt) / total_combinations_of_3
print("Probability that there will be one bulb of each type: {}".format(prob_one_bulb_of_each_type))
