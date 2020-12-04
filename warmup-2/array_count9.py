def array_count9(nums):
    """
    Given an array of ints, return the number of 9's in the array.

    >>> array_count9([1, 2, 9])
    1
    >>> array_count9([1, 9, 9])
    2
    >>> array_count9([1, 9, 9, 3, 9])
    3
    """
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
