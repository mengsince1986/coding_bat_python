def front_back(str):
    """
    Given a string, return a new string where the first and last chars have
    been exchanged.
    """
    result = str
    if len(str) > 1:
        result = str[-1] + str[1:-1] + str[0]
    return result

# tests
print(front_back('code'))
# 'eodc'
print(front_back('a'))
# 'a'
print(front_back('ab'))
# 'ba'
