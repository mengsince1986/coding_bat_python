def sorta_sum(a, b):
    """
    Given 2 ints, a and b, return their sum. However, sums in the range 10..19
    inclusive, are forbidden, so in that case just return 20.

    >>> sorta_sum(3, 4)
    7
    >>> sorta_sum(9, 4)
    20
    >>> sorta_sum(10, 11)
    21
    """
    result = a + b
    if 10 <= result <= 19:
        result = 20
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
