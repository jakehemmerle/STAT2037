# Jake Hemmerle

import collections
from math import floor


def get_frequency(number_array):
    # Returns dict with unique input array values as keys, number of each value as values
    return collections.Counter(number_array)


def get_relative_frequency(number_array):
    # Returns 'frequency of item' / 'total number of items'
    total_samples = sum(number_array)
    print("Total samples:  %d" % total_samples)

    rel_freq = {}
    for number in number_array:
        rel_freq[number] = number_array[number] / total_samples
    return rel_freq


def get_mean(number_array):
    # Returns the sum of values / total values
    sum = 0
    for value in number_array:
        sum += value
    return sum / len(number_array)


def get_median(array):
    """
    Sorts the array and returns the middle-most element

    >>> get_median([2, 4, 6, 8, 10])
    6.0

    >>> get_median([2, 5, 7, 8, 9, 12, 13, 23, 65])
    9.0

    >>> get_median([2, 4, 6, 8, 10, 12])
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


def count_decimals(number):
    # Returns number of decimals of a number
    string = str(number)
    if '.' not in string:
        return 0
    else:
        return string[::-1].find('.')


def get_sample_variance(array):
    # BROKEN?
    # Returns sample variance of the array
    mean = get_mean(array)
    return sum([(value - mean) ** 2 for value in array]) / len(array) - 1


def round_to_nearest_interval(array, interval):
    """
    Rounds all values in an array to the nearest interval value
    >>> round_to_nearest_interval([14, 33, 21], 5)
    [15, 35, 20]

    >>> round_to_nearest_interval([21, 24, 34], 2)
    [22, 24, 34]
    """
    floored_array = [value - value % interval for value in array]
    mod_array = [value % interval for value in array]
    final_array = []

    for base, mod in zip(floored_array, mod_array):
        if mod >= interval / 2:
            final_array.append(base + interval)
        else:
            final_array.append(base)

    return final_array
