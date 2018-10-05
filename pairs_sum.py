# How do you find all pairs of an integer array whose sum is equal to a given number?

def pairs_sum(array, s):
    numbers = set(array)
    res = []
    for x in numbers:
        y = abs(s-x)
        if y in numbers:
            res.append((x,y))
    return res

print(pairs_sum([-2,1,2,2,3,4,7], 5))
