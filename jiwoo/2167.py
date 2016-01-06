import sys

args = sys.stdin.readline()

args = map(int, args.split())
rows = args[0]
cols = args[1]
A = []
# Matrix initialization 
for i in range( rows ):
    line = map( int, sys.stdin.readline().split() )
    A.append(line)

# SubMatrix initialization
B = []
for i in range( rows ):
    B.append([])
    for j in range( cols ):
        B[i].append( 0 )

for i in range( rows ):
    if ( i != 0):
        B[i][0] = B[ i-1 ][ 0 ] + A[ i ][ 0 ] 
    else:
        B[i][0] = A[0][0]

for j in range( cols ):
    if ( j != 0 ):
        B[0][j] = B[0][ j -1 ] + A[0][j]
    else:
        B[0][j] = A[0][0]

for i in range(1, rows ):
    for j in range (1, cols ):
        B[i][j] = A[i][j] + B[i -1][j] + B[i][j-1] - B[i-1][j-1]

# Add padding B
B.insert(0, [0]*cols)
for r in range( rows + 1):
    B[r].insert(0, 0)


T = int (sys.stdin.readline())

for t in range ( T ):
    line = map( int, sys.stdin.readline().split() )
    x0 = line[0] - 1
    y0 = line[1] - 1
    x1 = line[2] 
    y1 = line[3] 


    result = B[x1][y1] - B[x0][y1] - B[x1][y0] + B[x0][y0]
    print result

