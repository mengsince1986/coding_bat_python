def caught_speeding(speed, is_birthday):
    """
    You are driving a little too fast, and a police officer stops you. Write
    code to compute the result, encoded as an int value: 0=no ticket, 1=small
    ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is
    between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the
    result is 2. Unless it is your birthday -- on that day, your speed can be 5
    higher in all cases.

    >>> caught_speeding(60, False)
    0
    >>> caught_speeding(65, False)
    1
    >>> caught_speeding(65, True)
    0
    """
    ticket = 0
    if is_birthday and 66 <= speed <= 85:
        ticket = 1
    elif is_birthday and speed >= 86:
        ticket = 2
    elif not is_birthday and 61 <= speed <= 80:
        ticket = 1
    elif not is_birthday and speed >= 81:
        ticket = 2
    return ticket

if __name__ == '__main__':
    import doctest
    doctest.testmod()
