import sys

r = sys.stdin.readline()

def dynfib( level, a0, a1):
    a_prev = a1
    a_cur = a0 + a1
    if ( level == 0 ):
        return a0
    else:
        return dynfib( level - 1, a_prev, a_cur )

for i in range( int(r) ):

    t = int( sys.stdin.readline() )

    a0 = dynfib( t, 1, 0 )
    a1 = dynfib( t, 0, 1 )

<<<<<<< HEAD
    print a0, a1
=======
    print a0, a1
>>>>>>> 65952fc85e9408314fd48e337d023479d8b0f8cd
