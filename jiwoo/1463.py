import sys

N = int( sys.stdin.readline() )



if N == 1 :
    print 0
elif N == 2:
    print 1
elif N == 3:
    print 1
else:
    an = [ 0 ] * (N + 1)
    an[ 1 ] = 0
    an[ 2 ] = 1
    an[ 3 ] = 1
    for i in range( 4, N + 1):
        cn = []

        if( i % 3 == 0):
            cn.append( an[i/3] + 1)
        if( i % 2 == 0 ):
            cn.append( an[i/2] + 1 )
        cn.append( an[ i - 1] + 1)

        an[i] = min( cn )
    print an[i]
