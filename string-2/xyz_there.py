def xyz_there(str):
    """
    Return True if the given string contains an appearance of "xyz" where the
    xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz"
    does not.

    >>> xyz_there('abcxyz')
    True
    >>> xyz_there('abc.xyz')
    False
    >>> xyz_there('xyz.abc')
    True
    """
    result = False
    found = False
    i = 0
    while not found and i < len(str) - 2:
        if str[i] == '.':
            i += 2
        else:
            word = str[i:i+3]
            if word == 'xyz':
                found = True
                result = True
            i += 1
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
