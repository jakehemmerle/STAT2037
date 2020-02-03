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
from stats import frequency, relative_frequency

keys = array_from_shitstring('1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17')
values = array_from_shitstring('740	204	127	50	33	28	19	19	6	7	6	7	4	4	5	3	3')
papers_and_freq = dict(zip(keys, values))

print(papers_and_freq)

at_least_5_papers = sum([papers_and_freq[key] for key in papers_and_freq if key >= 5])
at_least_10_papers = sum([papers_and_freq[key] for key in papers_and_freq if key >= 10])
more_than_10_papers = sum([papers_and_freq[key] for key in papers_and_freq if key > 10])
total_values = sum([papers_and_freq[key] for key in papers_and_freq])
print("at least 5 papers: {}".format(at_least_5_papers/total_values))
print("at least 10 papers: {}".format(at_least_10_papers/total_values))
print("more than 10 papers: {}".format(more_than_10_papers/total_values))
print("total values: {}".format(total_values))
