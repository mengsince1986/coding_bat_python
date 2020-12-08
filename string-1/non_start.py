def non_start(a, b):
    """
    Given 2 strings, return their concatenation, except omit the first char of
    each. The strings will be at least length 1.

    >>> non_start('Hello', 'There')
    'ellohere'
    >>> non_start('java', 'code')
    'avaode'
    >>> non_start('shotl', 'java')
    'hotlava'
    """
    return a[1:] + b[1:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
