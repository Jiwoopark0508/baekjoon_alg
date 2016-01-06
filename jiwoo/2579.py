import sys

T = int ( sys.stdin.readline() )
an = [0]
cn = [0] * (T+1)
for i in range( T ):
    an.append( int( sys.stdin.readline() ))

cn[ 1 ] = an [ 1 ]
cn[ 2 ] = an [ 1 ] + an[ 2 ]

for i in range( 3, T+1):
    cn[ i ] = an[ i ] + max(cn[i-2], cn[i-3]+an[i-1])

print cn[-1]