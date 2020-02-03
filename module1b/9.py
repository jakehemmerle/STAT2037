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

day = 10
swing = 8
graveyard = 6
total_workers = sum([day, swing, graveyard])

possible_from_day_shift = combinations(4, day)
possible_from_swing_shift = combinations(4, swing)
possible_from_graveyard_shift = combinations(4, graveyard)

total_possible_outcomes = combinations(4, total_workers)
print("number of possible from day shift: {}".format(possible_from_day_shift))

probability_all_day = possible_from_day_shift / total_possible_outcomes
probability_all_swing = possible_from_swing_shift / total_possible_outcomes
probability_all_graveyard = possible_from_graveyard_shift / total_possible_outcomes

print("Probability that all 4 are from day shift: {}".format(probability_all_day))
print("Probability that all 4 are from same shift: {}".format(sum([probability_all_day, probability_all_swing, probability_all_graveyard])))

from_at_least_two = total_possible_outcomes - possible_from_day_shift - possible_from_swing_shift - possible_from_graveyard_shift
print("From at least two shifts: {}".format(from_at_least_two / total_possible_outcomes))

from_day_and_swing = combinations(4, day + swing)
from_day_and_graveyard = combinations(4, day + graveyard)
from_swing_and_graveyard = combinations(4, swing + graveyard)

num_missing_one_shift = sum([from_day_and_swing, from_day_and_graveyard, from_swing_and_graveyard]) - sum([possible_from_day_shift, possible_from_swing_shift, possible_from_graveyard_shift])
prob_missing_one_shift = num_missing_one_shift / total_possible_outcomes
print("prob missing at least one shift: {}".format(prob_missing_one_shift))
