def alarm_clock(day, vacation):
    """
    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a
    boolean indicating if we are on vacation, return a string of the form
    "7:00" indicating when the alarm clock should ring. Weekdays, the alarm
    should be "7:00" and on the weekend it should be "10:00". Unless we are on
    vacation -- then on weekdays it should be "10:00" and weekends it should be
    "off".

    >>> alarm_clock(1, False)
    '7:00'
    >>> alarm_clock(5, False)
    '7:00'
    >>> alarm_clock(0, False)
    '10:00'
    """
    alarm = "off"
    if not vacation and 0 < day < 6:
        alarm = "7:00"
    elif not vacation and day in (0, 6):
        alarm = "10:00"
    elif vacation and 0 < day < 6:
        alarm = "10:00"
    return alarm

if __name__ == "__main__":
    import doctest
    doctest.testmod()
