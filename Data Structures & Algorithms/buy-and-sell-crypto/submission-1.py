class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        
        maxP = 0
        minP = prices[0]

        for i in range(1, len(prices), 1):
            if prices[i] < minP:
                minP = prices[i]
                continue
            
            maxP = max(maxP, prices[i] - minP)

        return maxP