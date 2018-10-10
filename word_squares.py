# https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares

def is_square(wl):
    l = len(wl)
    for w in wl:
        if len(w) != l:
            return False
    for i in range(l):
        for j in range(l):
            if wl[i][j] != wl[j][i]:
                return False
    return True

def word_squares(wl):
    d = dict()
    res = []
    for w in wl:
        l = len(w)
        if l not in d:
            d[l] = []
        d[l].append(w)
    for l in d:
        for w in d[l]:
            res += find_squares([w],d[l])
    return res

def find_squares(wl, w_set):
    l = len(wl)
    w = wl[0]
    n = len(w)
    # print(wl)
    if n == l:
        return [wl] if is_square(wl) else []
    res = []
    nth_words = [x for x in w_set if x[0] == w[l]]
    for x in nth_words:
        res += find_squares(wl+[x],w_set)
    return res

print(word_squares(["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]))
