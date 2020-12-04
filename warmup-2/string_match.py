def string_match(a, b):
    """
    Given 2 strings, a and b, return the number of the positions where they
    contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
    since the "xx", "aa", and "az" substrings appear in the same place in both
    strings.

    >>> string_match('xxcaazz', 'xxbaaz')
    3
    >>> string_match('abc', 'abc')
    2
    >>> string_match('abc', 'axc')
    0
    """
    shorter_len = min(len(a), len(b))
    count = 0
    i = 0
    while i + 1 < shorter_len:
        a_substr = a[i] + a[i+1]
        b_substr = b[i] + b[i+1]
        if a_substr == b_substr:
            count += 1
        i += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
