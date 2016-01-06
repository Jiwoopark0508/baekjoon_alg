import sys

case = int( sys.stdin.readline() )

values = []
for i in range( case ):
    values.append( map( int, sys.stdin.readline().split()))

result = []
result.append(values[0])
first_line = [ values[0][0] + values[1][0], values[0][0] + values[1][1]]
result.append(first_line)


for i in range( 2, case ):
    result.append([0]* (i+1) )
    for j in range( len(values[i]) ):
        if( j == 0 ):
            result[i][j] = values[i][j] + result[ i - 1 ][ j ]
        elif( j == (len (values[i]) - 1)):
            result[i][j] = values[i][j] + result[ i - 1 ][ j - 1]
        else:
            result[i][j] = values[i][j] + max( result[i-1][j-1], result[i-1][j])
print max(result[-1])