# https://techdevguide.withgoogle.com/resources/find-longest-word-in-dictionary-that-subsequence-of-given-string

def init_pdict(words):
    pdict = dict()
    for w in words:
        prefix = w[1][0]
        if prefix not in pdict:
            pdict[prefix] = [w]
        else:
            pdict[prefix].append(w)
    return pdict

def update_pdict(pdict, c):
    subsequences = []
    if c in pdict:
        l = pdict[c]
        pdict[c] = []
        for e in l:
            e[1] = e[1][1:]  # remove first character
            if e[1] == "":
                subsequences.append(e[0])
            else:
                prefix = e[1][0]
                if prefix not in pdict:
                    pdict[prefix] = [e]
                else:
                    pdict[prefix].append(e)
    return subsequences


def longest_subsequence(s, d):
    longest = (None, 0)
    words = [[id,d[id]] for id in range(len(d))]
    pdict = init_pdict(words)
    for c in s:
        subsequences = update_pdict(pdict, c)
        for sub in subsequences:
            w = d[sub]
            x = len(w)
            if x > longest[1]:
                longest = (w,x)
    return longest[0]

s = "abppplee"
d = ["able", "ale", "apple", "bale", "kangaroo"]
print(longest_subsequence(s,d))
