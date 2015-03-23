import random
import time


def print_time_to_execute(fn):
    """
    Decorator that will print the time it took for a method to execute after
    the method completes
    """
    def time_wrapper(*args, **kwargs):
        start = time.time()
        return_val = fn(*args, **kwargs)
        end = time.time()
        print 'Time to execute {}: {} seconds'.format(
            fn.__name__, end - start)
        return return_val
    return time_wrapper


def random_word(length=4, with_spaces=False):
    """
    Returns a random string of characters of a given length
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if with_spaces:
        alphabet += ' '
    return ''.join([random.choice(alphabet) for i in range(length)])


def assertEqual(*args):
    for i in range(len(args)):
        arg1 = args[i]
        arg2 = args[i - 1]
        if arg1 != arg2:
            raise AssertionError(
                '{} != {}'.format(arg1, arg2))
