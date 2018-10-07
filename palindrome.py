# How do you check if a given string is a palindrome?

def rec_palindrome(s):
    if len(s) < 2:
        res = True
    else:
        if s[0] != s[-1]:
            res = False
        else:
            res = palindrome(s[1:-1])
    return res

def palindrome(s):
    l = len(s)//2
    a, b = s[:l], s[l:]
    b = b[1:] if len(b) > len(a) else b  # odd len
    if a == b[::-1]:
        return True
    else:
        return False

print(rec_palindrome("aba"))
