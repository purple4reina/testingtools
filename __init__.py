import logging
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


def get_all_attrs(obj):
    """
    Runs getattr on all possible attributes on the obj, returning a dictionary
    of each attr and its value

    Excludes attributes that begin with an underscore
    """
    attr_dict = {}
    for attr in dir(obj):
        if attr.startswith('_'):
            continue
        val = getattr(obj, attr)
        attr_dict[attr] = val
    return attr_dict


class StopWatch(object):
    """
    A stopwatch to help print out timings.
    """
    def start(self):
        self.start = time.time()

    def stop(self):
        self.end = time.time()
        print '{} seconds'.format(self.end - self.start)


def set_loglevel_for_module(module, level):
    """
    Sets the log level for a given module.

    Level can be an integer representing the level as given in the logging
    module:
        CRITICAL 50
        ERROR    40
        WARNING  30
        INFO     20
        DEBUG    10
        NOTSET   0
    """
    logger = logging.getLogger(module)
    logger.setLevel(level)
