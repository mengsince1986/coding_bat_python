def sum2(nums):
    """
    Given an array of ints, return the sum of the first 2 elements in the
    array. If the array length is less than 2, just sum up the elements that
    exist, returning 0 if the array is length 0.

    >>> sum2([1, 2, 3])
    3
    >>> sum2([1, 1])
    2
    >>> sum2([1, 1, 1, 1])
    2
    """
    result = 0
    i = 0
    while i < len(nums) and i < 2:
        result += nums[i]
        i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
