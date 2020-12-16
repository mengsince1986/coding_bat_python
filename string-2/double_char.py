def double_char(str):
    """
    Given a string, return a string where for every char in the original, there
    are two chars.

    >>> double_char('The')
    'TThhee'
    >>> double_char('AAbb')
    'AAAAbbbb'
    >>> double_char('Hi-There')
    'HHii--TThheerree'
    """
    result = ''
    for char in str:
        result += char * 2
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
