"""
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c

  return sum
"""

def lone_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum. However, if one of the values
    is the same as another of the values, it does not count towards the sum.

    >>> lone_sum(1, 2, 3)
    6
    >>> lone_sum(3, 2, 3)
    2
    >>> lone_sum(3, 3, 3)
    0
    """
    if a == b and b == c:
        result = 0
    elif a == b:
        result = c
    elif b == c:
        result = a
    elif a == c:
        result = b
    else:
        result = a + b + c
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
