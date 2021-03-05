def fib(n: int, k: int) -> int:
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a * k + b
    return b


n = 5
k = 3

print(fib(n, k))
