def assertEqual(*args):
    for i in xrange(len(args)):
        arg1 = args[i]
        arg2 = args[i - 1]
        if arg1 != arg2:
            raise AssertionError(
                '{} != {}'.format(arg1, arg2))


def assertRaises(exception_class, function, *funargs, **funkwargs):
    """
    Given an exception class and a function along with any args to the
    function, assert that the exception is raised when the function is
    executed.
    """
    try:
        function(*funargs, **funkwargs)
    except exception_class:
        # everything worked as expected
        return
    except:
        # some other error was raised, this case will be handled below
        pass
    raise AssertionError(
        '{} with args {} and kwargs {} should have raised {}'.format(
            function.__name__,
            funargs or '()', funkwargs or '()',
            exception_class.__name__)
    )
