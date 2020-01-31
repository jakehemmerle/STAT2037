import sys
sys.path.insert(1, '..')
from utils.webassign import array_from_shitstring

shitstring = "5.6	7.2	7.3	6.3	8.1	6.8	7.0	7.6	6.8	6.5	7.0	6.3	7.9	9.0 8.2	8.7	7.8	9.7	7.4	7.7	9.7	7.8	7.7	11.6	11.5	11.8	10.6"

array = array_from_shitstring(shitstring)

for number in array:
    print(number)
