import pdb

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

print(fibonacci(10))

