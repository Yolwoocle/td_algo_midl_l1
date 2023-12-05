def fibo(n: int) -> tuple:
    if n == 0:
        return (0, 1)
    else:
        a, b = fibo(n-1)
        return (b, a+b)
    
for i in range(10):
    print(i, fibo(i))