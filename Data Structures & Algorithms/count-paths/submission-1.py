class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Choice 1: go down n-1 times
        # Choice 2: go right m-1 times

        # if 1x1 return 1 only one "path" to get to 0,0
        # if 1x2 return 1 only one path to get to 0,1: right
        # if 2x1 return 1 only one way to get to 1,0: down
        # if 2x2 return 2 two ways 

        # so for each case we need to remember the top and left cells or just add 1
        if m==1 or 1==n:
            return 1


        dp = [[0]*n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], 1) + max(dp[i-1][j], 1)

        return dp[m-1][n-1]