# Jake Hemmerle

import collections
from math import floor, sqrt, factorial


def frequency(number_array):
    # Returns dict with unique input array values as keys, number of each value as values
    return dict(collections.Counter(number_array))


def relative_frequency(frequency_array):
    # Returns 'frequency of item' / 'total number of items'
    total_samples = sum([frequency_array[key] for key in frequency_array])
    print("Total samples:  %d" % total_samples)

    rel_freq = {}
    for number in frequency_array:
        rel_freq[number] = frequency_array[number] / total_samples
    return rel_freq


def mean(number_array):
    # Returns the sum of values / total values
    sum = 0
    for value in number_array:
        sum += value
    return sum / len(number_array)


def deviation_from_mean(number_array):
    """
    calculate mean on a list and return each point's deviation
    """
    calculated_mean = mean(number_array)
    deviation_list = [number - calculated_mean for number in number_array]
    return deviation_list


def median(number_array):
    """
    Sorts the array and returns the middle-most element

    >>> median([2, 4, 6, 8, 10])
    6.0

    >>> median([2, 5, 7, 8, 9, 12, 13, 23, 65])
    9.0

    >>> median([2, 4, 6, 8, 10, 12])
    7.0
    """
    number_array.sort()
    halfway_point = floor(len(number_array) / 2)
    if len(number_array) % 2 == 0:
        return float((number_array[halfway_point - 1] + number_array[halfway_point]) / 2)
    else:
        return float(number_array[halfway_point])


def get_range(number_array):
    # Returns distance between largest and smallest elements
    return max(number_array) - min(number_array)


def variance(number_array):
    # Returns sample variance of the array (the s**2)
    data_mean = mean(number_array)
    sample_variance = [(value - data_mean) ** 2 for value in number_array]
    return sum(sample_variance) / (len(number_array) - 1)


def standard_deviation(number_array):
    return sqrt(variance(number_array))


def permutations(k, n):
    return factorial(n) / factorial(n - k)


def combinations(k, n):
    return permutations(k, n) / factorial(k)


# TODO: complete this function
def inclusion_exclusion(array):
    """
    returns union of array of sets, array being:
    [len(set) for set in sets]
    example would be [2, 3, 4] first set having 2 elements, second having 3, etc.
    """
