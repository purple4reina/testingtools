def prod(num_list):
    """
    Returns the product of all numbers in num_list

    >>> prod([3, 4])
    12
    >>> prod([1, 2, 3])
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


def prime_iter(*args):
    """
    Iterator that returns a prime numbers

    The arguments are similar arguments as given to range:
        prime_iter([min,] max)
    """
    if len(args) == 1:
        min = 3
        max = args[0]
    elif len(args) == 2:
        min = args[0]
        max = args[1]
    else:
        raise ValueError('Incorrect number of arguments')

    # We want the min value to be odd and at least 3 so that the iterator below
    # can be most performant
    if min < 3:
        min = 3
    elif not min % 2:
        min += 1

    yield 2
    for num in xrange(min, max, 2):
        if is_prime(num):
            yield num


def is_prime(num):
    """
    Boolean if the number is prime or not
    """
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif not num % 2:
        return False
    for n in xrange(3, int(num ** 0.5) + 2, 2):
        if not num % n:
            return False
    return True
