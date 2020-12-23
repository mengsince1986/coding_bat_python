def has22(nums):
    """
    Given an array of ints, return True if the array contains a 2 next to a 2
    somewhere.

    >>> has22([1, 2, 2])
    True
    >>> has22([1, 2, 1, 2])
    False
    >>> has22([2, 1, 2])
    False
    """
    i = 0
    found_22 = False
    while not found_22 and i < len(nums) - 1:
        if nums[i] == 2 and nums[i+1] == 2:
            found_22 = True
        else:
            i += 1
    return found_22

if __name__ == '__main__':
    import doctest
    doctest.testmod()
