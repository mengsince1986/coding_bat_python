def pos_neg(a, b, negative):
    """
    Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both
    are negative.
    """
    is_different_signs = a * b < 0
    is_both_negative = a < 0 and b < 0
    return (not negative and is_different_signs) or (negative and
                                                     is_both_negative)

# tests
print(pos_neg(1, -1, False))
# True
print(pos_neg(-1, 1, False))
# True
print(pos_neg(-4, -5, True))
# True
