def make_chocolate(small, big, goal):
    """
    We want make a package of goal kilos of chocolate. We have small bars (1
    kilo each) and big bars (5 kilos each). Return the number of small bars to
    use, assuming we always use big bars before small bars. Return -1 if it
    can't be done.

    >>> make_chocolate(4, 1, 9)
    4
    >>> make_chocolate(4, 1, 10)
    -1
    >>> make_chocolate(4, 1, 7)
    2
    """
    if goal > small + big * 5:
        result = -1
    elif goal % 5 > small:
        result = -1
    elif goal >= big * 5:
        result = goal - big * 5
    else:
        result = goal % 5
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
