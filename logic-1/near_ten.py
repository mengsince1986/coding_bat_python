def near_ten(num):
    """
    Given a non-negative number "num", return True if num is within 2 of a
    multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 %
    5) is 2. See also:

    >>> near_ten(12)
    True
    >>> near_ten(17)
    False
    >>> near_ten(19)
    True
    """
    result = False
    remainder = num % 10
    if remainder <= 2 or remainder >= 8:
        result = True
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
