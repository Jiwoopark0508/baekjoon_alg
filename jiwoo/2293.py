import sys

n, target = map( int, sys.stdin.readline().split() )

ways = [0] * (target + 1)
coins = []
for i in range( n ):
    coin = int( sys.stdin.readline() )
    coins.append( coin )

# ways initialize
ways[ 0 ] = 1


for coin in coins:
    for i in range( coin, target + 1):
        if( i - coin >= 0):
            ways[ i ] = ways[ i ] + ways[ i - coin ]

print ways[-1]
