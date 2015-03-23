def prod(*num_list):
    """
    Returns the product of all numbers in num_list

    >>> prod(3, 4)
    12
    >>> prod(1, 2, 3)
    6
    """
    product = 1
    for num in num_list:
        product *= num
    return product


def largest(*args):
    """
    Returns the largest value
    """
    large = args[0]
    for arg in args:
        if arg > large:
            large = arg
    return large
biggest = largest  # synonym


def smallest(*args):
    """
    Returns the smallest value
    """
    small = args[0]
    for arg in args:
        if arg < small:
            small = arg
    return small
