def lucky_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if one of the values
    is 13 then it does not count towards the sum and values to its right do not
    count. So for example, if b is 13, then both b and c do not count.

    >>> lucky_sum(1, 2, 3)
    6
    >>> lucky_sum(1, 2, 13)
    3
    >>> lucky_sum(1, 13, 3)
    1
    """
    result = 0
    if a != 13:
        result += a
    if a != 13 and b != 13:
        result += b
    if a != 13 and b != 13 and c != 13:
        result += c
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
