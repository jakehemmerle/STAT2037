# Jake Hemmerle


def array_from_multiline_shitfile(filename) -> list:
    """
    Paste those red numbers from Webassign in a file, call this function with filename.
    Returns a list with those numbers.
    data = array_from_multiline_shitfile('shitfile.txt')
    """
    shitfile = open(filename, 'r')
    shitstring = shitfile.read()
    return array_from_shitstring(shitstring)


def array_from_shitstring(shitstring) -> list:
    """
    Returns a list of numbers from a nasty formatted copied-from-Webassign string (same as above, just raw string as input)
    """
    string = shitstring.strip()
    string_array = string.split()
    number_array = []
    for number in string_array:
        number_array.append(int(number))

    return number_array

def array_from_shitstring_floats(shitstring) -> list:
    """
    Returns a list of numbers from a nasty formatted copied-from-Webassign string (same as above, just raw string as input)
    """
    string = shitstring.strip()
    string_array = string.split()
    number_array = []
    for number in string_array:
        number_array.append(float(number))

    return number_array
