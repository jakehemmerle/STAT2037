# Jake Hemmerle

import collections
from math import floor


def frequency(number_array):
    # Returns dict with unique input array values as keys, number of each value as values
    return collections.Counter(number_array)


def relative_frequency(number_array):
    # Returns 'frequency of item' / 'total number of items'
    total_samples = sum(number_array)
    print("Total samples:  %d" % total_samples)

    rel_freq = {}
    for number in number_array:
        rel_freq[number] = number_array[number] / total_samples
    return rel_freq


def mean(number_array):
    # Returns the sum of values / total values
    sum = 0
    for value in number_array:
        sum += value
    return sum / len(number_array)


def median(array):
    """
    Sorts the array and returns the middle-most element

    >>> median([2, 4, 6, 8, 10])
    6.0

    >>> median([2, 5, 7, 8, 9, 12, 13, 23, 65])
    9.0

    >>> median([2, 4, 6, 8, 10, 12])
    7.0
    """
    array.sort()
    halfway_point = floor(len(array) / 2)
    if len(array) % 2 == 0:
        return float((array[halfway_point - 1] + array[halfway_point]) / 2)
    else:
        return float(array[halfway_point])


def get_range(array):
    # Returns distance between largest and smallest elements
    return max(array) - min(array)


def sample_variance(array):
    # BROKEN?
    # Returns sample variance of the array
    data_mean = mean(array)
    return sum([(value - data_mean) ** 2 for value in array]) / len(array) - 1
