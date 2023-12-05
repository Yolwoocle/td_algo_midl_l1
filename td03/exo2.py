def log2(n):
    assert n > 0

    k = 0
    assert 2**k <= n
    while (2**k > n or n >= 2**(k+1)):
        k += 1
        assert 2**k <= n and k >= 0
    assert 2**k <= n < 2**(k+1) and k >= 0
    return k

print(log2(0))
print(log2(1))
print(log2(2))
print(log2(4))
print(log2(6))
print(log2(8))
print(log2(12))
print(log2(16))
print(log2(-345))
print(log2(-2))