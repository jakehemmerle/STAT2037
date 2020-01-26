import sys

# allows import of project files (idk how else to do this)
sys.path.insert(1, '..')
from utils.webassign import array_from_shitstring
from stats import round_to_nearest_interval, median

actual_pressure = array_from_shitstring(
    "128.6  	137.8  	148.4  	140.0  	123.7  	132.0  	118.3  	141.5  	143.2 ")
actual_pressure.sort()
print("Actual pressure: {}".format(actual_pressure))

rounded_pressure = round_to_nearest_interval(actual_pressure, 5)
print("Rounded pressure: {0}".format(rounded_pressure))

median_rounded_pressure = median(rounded_pressure)
print("Median (rounded pressure): {0}".format(median_rounded_pressure))
