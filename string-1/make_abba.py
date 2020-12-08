def make_abba(a, b):
    """
    Given two strings, a and b, return the result of putting them together in
    the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

    >>> make_abba('Hi', 'Bye')
    'HiByeByeHi'
    >>> make_abba('Yo', 'Alice')
    'YoAliceAliceYo'
    >>> make_abba('What', 'Up')
    'WhatUpUpWhat'
    """
    return a + b + b + a

if __name__ == '__main__':
    import doctest
    doctest.testmod()
