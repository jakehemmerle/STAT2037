import sys

# allows import of project files (idk how else to do this)
sys.path.insert(1, '..')
from utils.webassign import array_from_shitstring
from stats import mean

youngs_mod = array_from_shitstring(" 116.6 115.8 114.9 115.3 115.6 ")
youngs_mod.sort()
print("Young's Mod: {}".format(youngs_mod))

sample_mean = mean(youngs_mod)
print("Young's Mod (mean): {}".format(sample_mean))


