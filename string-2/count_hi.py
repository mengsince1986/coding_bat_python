def count_hi(str):
    """
    Return the number of times that the string "hi" appears anywhere in the
    given string.

    >>> count_hi('abc hi ho')
    1
    >>> count_hi('ABChi hi')
    2
    >>> count_hi('hihi')
    2
    """
    result = 0
    i = 0
    while i < len(str) - 1:
        if str[i] == 'h'and str[i+1] == 'i':
            result += 1
            i += 2
        else:
            i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
