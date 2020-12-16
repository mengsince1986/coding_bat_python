def count_code(str):
    """
    Return the number of times that the string "code" appears anywhere in the
    given string, except we'll accept any letter for the 'd', so "cope" and
    "cooe" count.

    >>> count_code('aaacodebbb')
    1
    >>> count_code('codexxcode')
    2
    >>> count_code('cozexxcope')
    2
    """
    result = 0
    i = 0
    while i < len(str) - 3:
        word = str[i:i+4]
        if word[:2] == 'co' and word[-1] == 'e':
            result += 1
            i += 4
        else:
            i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
