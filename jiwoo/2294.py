import sys

n, k = map( int, sys.stdin.readline().split() )

coins = []
ways = [ -1 ] * ( k + 1)

for i in range( n ):
    coins.append( int( sys.stdin.readline() ))

coins.sort()



for i in range( k + 1):
    if( i % coins[ 0 ] == 0 ):
        ways[ i ] = i / coins[0]

coins.remove( coins [ 0 ])

for coin in coins:
    for i in range( k + 1 ):
        if ( i % coin == 0 ):
            ways[ i ] = i / coin
        
        elif( i > coin ):
            if( ways[ i ] == -1 and ways[ i - coin ] == -1 ):
                ways[ i ] = -1

            elif( ways[ i - coin] == -1 ):
                ways[ i ] = ways[ i ]
            elif( ways[ i ] == -1 ):
                ways[ i ] = ways[i - coin] + 1
            else:
                ways[ i ] = min ( ways[ i ] , ways[ i-coin ] + 1)

print ways[ k ]