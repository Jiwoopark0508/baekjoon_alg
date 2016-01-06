import sys

r = sys.stdin.readline()

def min_j(j, arr):
    sublist = []
    for i in range( len(arr) ):
        if( i != j ):
            sublist.append( arr[i] )
    return min(sublist)

flag = 0


for i in range( int(r) ):
    t1 = map(int, sys.stdin.readline().split())

    if( flag == 0 ):
        t2 = t1
        flag = 1

    else:
        t_temp = []
        #copy t2 -> t_temp
        for i in range( len( t2 ) ):
            t_temp.append( t2[i] )

        for j in range( 3 ):
            t2[j] = t1[j] + min_j(j, t_temp)

print min(t2)