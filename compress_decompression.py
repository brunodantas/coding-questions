# https://techdevguide.withgoogle.com/resources/compress-decompression

import sys

def get_context(s, start):
    open = 1
    for i in range(start,len(s)):
        if s[i] == '[':
            open += 1
        elif s[i] == ']':
            open -= 1
        if open == 0:
            break
    return i

def compress_decompression(s):
    if s == "":
        return ""
    res = ""
    number = ""
    for i in range(len(s)):
        if s[i].isdigit():
            number += s[i]
        else:
            break
    if s[i] == '[':
        start = i+1
        end = get_context(s,start)
        n = 1 if number == "" else int(number)
        res = n*compress_decompression(s[start:end])
        return res + compress_decompression(s[end+1:])
    else:
        res = s[i:]
        return res


if __name__ == '__main__':
        print(compress_decompression(sys.argv[1]))
