def sum67(nums):
    """
    Return the sum of the numbers in the array, except ignore sections of
    numbers starting with a 6 and extending to the next 7 (every 6 will be
    followed by at least one 7). Return 0 for no numbers.

    >>> sum67([1, 2, 2])
    5
    >>> sum67([1, 2, 2, 6, 99, 99, 7])
    5
    >>> sum67([1, 1, 6, 7, 2])
    4
    """
    result = 0
    i = 0
    is_ignored = False
    while i < len(nums):
        if str(nums[i])[0] == '6':
            is_ignored = True
            i += 1
        elif is_ignored:
            if nums[i] == 7:
                is_ignored = False
            i += 1
        else:
            result += nums[i]
            i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
