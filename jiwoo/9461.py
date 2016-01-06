import sys

def dynfib( level, a0, a1, a2 ):
    
    if( level == 0 ):
        return a0 + a1
    elif( level == -1 ):
        return a2
    elif( level == -2 ):
        return a1
    elif( level == -3 ):
        return a0
    else:
        return dynfib( level - 1, a1, a2, a0+ a1)


for i in range ( int( sys.stdin.readline() )):
    c = int(sys.stdin.readline())
    print dynfib( c - 4, 1, 1, 1)