def assertEqual(*args):
    for i in range(len(args)):
        arg1 = args[i]
        arg2 = args[i - 1]
        if arg1 != arg2:
            raise AssertionError(
                '{} != {}'.format(arg1, arg2))
