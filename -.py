def move_hyphen(s):
    if s is None:
        return None

    hyphens = s.count('-')
    result = '-' * hyphens

    for ch in s:
        if ch != '-':
            result += ch

    return result


# test
s = input("enter string: ")
print("Original:", s)
print("Modified:", move_hyphen(s))
