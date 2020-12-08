def without_end(str):
    """
    Given a string, return a version without the first and last char, so
    "Hello" yields "ell". The string length will be at least 2.

    >>> without_end('Hello')
    'ell'
    >>> without_end('java')
    'av'
    >>> without_end('coding')
    'odin'
    """
    return str[1:-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
