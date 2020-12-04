def array123(nums):
    """
    Given an array of ints, return True if the sequence of numbers 1, 2, 3
    appears in the array somewhere.

    >>> array123([1, 1, 2, 3, 1])
    True
    >>> array123([1, 1, 2, 4, 1])
    False
    >>> array123([1, 1, 2, 1, 2, 3])
    True
    """
    found_123 = False
    i = 0
    while not found_123 and i + 2 < len(nums):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            found_123 = True
        i += 1
    return found_123

if __name__ == '__main__':
    import doctest
    doctest.testmod()
