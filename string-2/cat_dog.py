def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times
    in the given string.

    >>> cat_dog('catdog')
    True
    >>> cat_dog('catcat')
    False
    >>> cat_dog('1cat1cadodog')
    True
    """
    cat_count = 0
    dog_count = 0
    i = 0
    while i < len(str) - 2:
        word = str[i:i+3]
        if word == 'cat':
            cat_count += 1
            i += 3
        elif word == 'dog':
            dog_count += 1
            i += 3
        else:
            i += 1
    return cat_count == dog_count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
