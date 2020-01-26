import sys
sys.path.insert(1, '..')
from utils.webassign import array_from_shitstring

particles_shit = "0	    1	    2	    3	    4	    5	    6	    7	    8	    9	    10	    11	    12	    13	    14"
freq_shit = "1 1 3 12 11 15 20 10 9 4 5 3 3 2 1"

particles = array_from_shitstring(particles_shit)
freq = array_from_shitstring(freq_shit)

together = dict(zip(particles, freq))
print(together)

at_least_5 = [value for key, value in together.items() if key >= 5]
print("Values above 5: {0}".format(at_least_5))

print("Sum: {}".format(sum(at_least_5)))


inclusive = [value for key, value in together.items() if 5 <= key <= 10]
exclusive = [value for key, value in together.items() if 5 < key < 10]
print("Between 5 and 10, inclusive: {}".format(sum(inclusive)))
print("Between 5 and 10, exclusive: {}".format(sum(exclusive)))
