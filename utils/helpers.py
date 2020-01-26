

def count_decimals(number):
    # Returns number of decimals of a number
    string = str(number)
    if '.' not in string:
        return 0
    else:
        return string[::-1].find('.')


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
