
def Fibonacci(n: int):
    pair = [0,1]
    for x in range(n): pair.append(pair[x]+pair[x+1])
    return pair[-2]


print(Fibonacci(int(input())))




