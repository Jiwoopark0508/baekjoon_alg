import sys

def an( n, a0, a1):
    if( n == 1):
        return a0
    else:
        return an( n - 1, a1, a0 + a1)

n = int ( sys.stdin.readline())

print an(n, 0, 1) + an(n, 1, 0)