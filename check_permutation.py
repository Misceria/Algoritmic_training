
from collections import Counter

def checkPermutation(a):
    cnt = Counter(a)
    ans = (max(a) == len(a) and max(cnt.values()) == 1)
    print("OK" if ans else "BAD")


a = list(map(int, input().split(" ")))
checkPermutation(a)




