def make_out_word(out, word):
    """
    Given an "out" string length 4, such as "<<>>", and a word, return a new
    string where the word is in the middle of the out string, e.g. "<<word>>".

    >>> make_out_word('<<>>', 'Yay')
    '<<Yay>>'
    >>> make_out_word('<<>>', 'WooHoo')
    '<<WooHoo>>'
    >>> make_out_word('[[]]', 'word')
    '[[word]]'
    """
    return out[:2] + word + out[-2:]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
