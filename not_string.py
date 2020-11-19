def not_string(str):
    """
    Given a string, return a new string where "not " has been added to the
    front. However, if the string already begins with "not", return the string
    unchanged.
    """
    not_str = str
    if not_str.split()[0] != 'not':
        not_str = 'not ' + not_str
    return not_str

# tests
print(not_string('candy'))
# 'not candy'
print(not_string('x'))
# 'not x'
print(not_string('not bad'))
# 'not bad'
