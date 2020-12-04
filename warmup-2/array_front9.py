def array_front9(nums):
    """
    Given an array of ints, return True if one of the first 4 elements in the
    array is a 9. The array length may be less than 4.

    >>> array_front9([1, 2, 9, 3, 4])
    True
    >>> array_front9([1, 2, 3, 4, 9])
    False
    >>> array_front9([1, 2, 3, 4, 5])
    False
    """
    found = False
    i = 0
    while not found and i < 4 and i < len(nums):
        if nums[i] == 9:
            found = True
        i += 1
    return found

if __name__ == '__main__':
    import doctest
    doctest.testmod()
