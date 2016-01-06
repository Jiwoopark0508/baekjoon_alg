import sys

r = int( sys.stdin.readline() )

values = map( int, sys.stdin.readline().split())
cum_sum = []

min_ref = 0

for num in values:
    
    if( len(cum_sum) > 0):
        cum_sum.append(num + cum_sum[-1])    
    else:
        cum_sum.append(num)


result = [0]


for sums in cum_sum:
    
    result.append( sums - min_ref )

    if( sums < min_ref):
        min_ref = sums 

print max(result)