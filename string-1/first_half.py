def first_half(str):
    """
    Given a string of even length, return the first half. So the string
    "WooHoo" yields "Woo".

    >>> first_half('WooHoo')
    'Woo'
    >>> first_half('HelloThere')
    'Hello'
    >>> first_half('abcdef')
    'abc'
    """
    return str[:int(len(str)/2)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
