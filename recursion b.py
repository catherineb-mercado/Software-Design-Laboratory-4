# Recursive algorithm to compute
# integer part of base 2 logarithm of n.
def log_base2(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return 1 + log_base2(n//2)
