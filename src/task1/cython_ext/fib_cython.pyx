def fib(int n):
    value = fib(n-1) + fib(n-2) if n > 1 else n
    return value