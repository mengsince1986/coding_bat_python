def hello_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello
    Bob!".

    >>> hello_name('Bob')
    'Hello Bob!'
    >>> hello_name('Alice')
    'Hello Alice!'
    >>> hello_name('X')
    'Hello X!'
    """
    return "Hello {}!".format(name)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
