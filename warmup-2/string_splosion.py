def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    >>> string_splosion('Code')
    'CCoCodCode'
    >>> string_splosion('abc')
    'aababc'
    >>> string_splosion('ab')
    'aab'
    """
    result = ""
    for i in range(len(str)):
        for j in range(i+1):
            result += str[j]
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
