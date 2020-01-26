import sys

sys.path.insert(1, '..')
from utils.webassign import array_from_shitstring
from utils.arrays import round_to_nearest_interval

actual_pressure = array_from_shitstring(
    "128.6  	137.4  	148.4  	140.0  	123.7  	132.0  	118.3  	141.5  	143.2 ")
actual_pressure.sort()
print("Actual pressure: {}".format(actual_pressure))

rounded_pressure = round_to_nearest_interval(actual_pressure, 5)
print("Rounded pressure: {0}".format(rounded_pressure))
