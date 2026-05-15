class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prevs = 2
        prev = 3
        for i in range(4,n+1):
            prevs, prev = prev, prev + prevs
        return prev
