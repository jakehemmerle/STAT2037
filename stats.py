# Jake Hemmerle

import collections
from math import floor, sqrt, factorial


def frequency(data_list):
    # Returns dict with unique input array values as keys, number of each value as values
    return dict(collections.Counter(data_list))


def relative_frequency(data_list):
    # Returns 'frequency of item' / 'total number of items'
    total_samples = sum([data_list[key] for key in data_list])
    print("Total samples:  %d" % total_samples)

    rel_freq = {}
    for number in data_list:
        rel_freq[number] = data_list[number] / total_samples
    return rel_freq


def mean(data_list):
    # Returns the sum of values / total values
    sum = 0
    for value in data_list:
        sum += value
    return sum / len(data_list)


def trimmed_mean(data_list, trim):
    """
    trim is a value between 0 and .5
    >>> trimmed_mean([14.7, 12.9, 17.5, 14.2, 12.1, 11.0, 9.3, 8.0], .125)
    12.366666666666667
    """

    trim_index = floor(trim * len(data_list))
    trimmed_array = data_list[trim_index:-trim_index]
    return mean(trimmed_array)


def deviation_from_mean(data_list):
    """
    calculate mean on a list and return each point's deviation
    """
    calculated_mean = mean(data_list)
    deviation_list = [number - calculated_mean for number in data_list]
    return deviation_list


def median(data_list):
    """
    Sorts the array and returns the middle-most element

    >>> median([2, 4, 6, 8, 10])
    6.0

    >>> median([2, 5, 7, 8, 9, 12, 13, 23, 65])
    9.0

    >>> median([2, 4, 6, 8, 10, 12])
    7.0
    """
    data_list.sort()
    halfway_point = floor(len(data_list) / 2)
    if len(data_list) % 2 == 0:
        return float((data_list[halfway_point - 1] + data_list[halfway_point]) / 2)
    else:
        return float(data_list[halfway_point])


def get_range(data_list):
    # Returns distance between largest and smallest elements
    return max(data_list) - min(data_list)


def variance(data_list):
    # Returns sample variance of the array (the s**2)
    data_mean = mean(data_list)
    sample_variance = [(value - data_mean) ** 2 for value in data_list]
    return sum(sample_variance) / (len(data_list) - 1)


def standard_deviation(data_list):
    return sqrt(variance(data_list))


def permutations(k, n):
    return factorial(n) / factorial(n - k)


def combinations(k, n):
    return permutations(k, n) / factorial(k)


# TODO: complete this function
def inclusion_exclusion(set_list):
    """
    returns union of array of sets, array being:
    [len(set) for set in sets]
    example would be [2, 3, 4] first set having 2 elements, second having 3, etc.
    """
