# setup
import sys

sys.path.insert(1, '..')
from utils.webassign import array_from_shitstring
from stats import get_mean, get_median

# string to array
urban = array_from_shitstring("6.0	5.0	11.0	33.0	4.0	5.0	80.0	18.0	35.0	17.0	23.0	")
farm = array_from_shitstring(
    "4.0	12.0	10.0	7.0	9.0	8.0	3.0	20.0	3.0	9.3	21.0	9.1	2.0	1.0	0.1")
urban.sort()
farm.sort()
print("Urban: {}".format(urban))
print("Farm: {}".format(farm))

# determine sample mean for each
print("Concentration mean for urban homes (EU/mg): {}".format(get_mean(urban)))
print("Concentration mean for farm homes (EU/mg): {}".format(get_mean(farm)))

# determine sample median for each
print("Sample median for urban homes (EU/mg): {}".format(get_median(urban)))
print("Sample median for farm homes (EU/mg): {}".format(get_median(farm)))

# calculate trimmed mean by dropping first and last elements
urban.sort()
farm.sort()

# trim
urban_trimmed = urban[1:-1]
farm_trimmed = farm[1:-1]

print("Trimmed mean for urban homes (EU/mg): {}".format(get_mean(urban_trimmed)))
print("Trimmed mean for farm homes (EU/mg): {}".format(get_mean(farm_trimmed)))

# trimmed percentages
print("Urban trimmed: {}".format(2 / len(urban) / 2))
print("Farm trimmed: {}".format(2 / len(farm) / 2))
