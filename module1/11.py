import sys

# allows import of project files (idk how else to do this)
sys.path.insert(1, '..')
from utils.webassign import array_from_shitstring
from stats import mean, deviation_from_mean, variance, standard_deviation

youngs_mod = array_from_shitstring(" 116.6 115.8 114.9 115.3 115.6 ")
youngs_mod.sort()
print("Young's Mod: {}".format(youngs_mod))

sample_mean = mean(youngs_mod)
print("Young's Mod (mean): {}".format(sample_mean))

print("Deviation from mean:")
deviation_list = deviation_from_mean(youngs_mod)
for data_point, deviation in zip(youngs_mod, deviation_list):
    print("Sample: {0}, deviation from mean: {1}".format(data_point, deviation))

my_variance = variance(youngs_mod)
print("Sample variance: {}".format(my_variance))
print("Standard deviation: {}".format(standard_deviation(youngs_mod)))
