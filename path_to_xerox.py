


def PathToXerox(n: int, k:int):
    a = [abs(n-k*(max(n//k, 1))), abs(n-k*(max(n//k,1)+1))]
    return min(a)

print(PathToXerox(4, 10))