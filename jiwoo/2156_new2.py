import sys

T = int ( sys.stdin.readline() )
wine = [0] * (T+1)
dp = [0] * (T+1)
max_value = 0
for i in range( T ):
    wine[i] = int( sys.stdin.readline() )

    dp[ 0 ] = wine[0]
    dp[ 1 ] = dp[0]+ wine[1]

    max_value = max( dp[0], dp[1])

for i in range(2, T):
    dp[i] = wine[i] + max(dp[i - 2], dp[i - 3] + wine[i - 1])
    dp[i] = max(dp[i], dp[i - 1])
    max_value = max( max_value, dp[i])

print max_value