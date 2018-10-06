# How do you find all permutations of a string?

def permutations(s):
    if len(s) < 2:
        return s
    h, t = s[0], s[1:]
    ptail = permutations(s[1:])  # permutations of the tail
    res = []
    for e in ptail:
        res += permut_insert(h, e)
    return res

def permut_insert(c, s):
    res = []
    for l in range(len(s)+1):
        res.append(s[:l] + c + s[l:])
    return res

p = permutations("abc")
print(len(p), p)
