import math

def rec(string, vowels):
    if len(string) == 0:
        return 0
    elif len(string) == 1:
        return 1
    else:
        sum1 = 0
        vo = 0
        co = 0
        for e in string:
            if e in vowels:
                vo += 1
            else:
                co += 1
        sum1 += abs(vo - co)
        s1 = string[: math.floor(len(string)/2)]
        s2 = string[math.floor(len(string)/2):]

        sum2 = rec(s1) + rec(s2)
        return sum1 + sum2

def f():
    print(rec('sample', vowels = 'aeiou'))



f()