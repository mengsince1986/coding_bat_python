def make_bricks(small, big, goal):
    """
    We want to make a row of bricks that is goal inches long. We have a number
    of small bricks (1 inch each) and big bricks (5 inches each). Return True
    if it is possible to make the goal by choosing from the given bricks. This
    is a little harder than it looks and can be done without any loops.

    >>> make_bricks(3, 1, 8)
    True
    >>> make_bricks(3, 1, 9)
    False
    >>> make_bricks(3, 2, 10)
    True
    """
    result = True
    # fail 1 -- not enough
    if goal > small + big * 5:
        result = False
    elif goal % 5 > small:
        result = False
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
