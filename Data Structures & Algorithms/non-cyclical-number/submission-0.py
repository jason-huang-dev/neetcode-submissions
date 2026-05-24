class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSum(n:int)->int:
            sum = 0
            for num in str(n):
                sum += int(num)**2
            return sum

        nums = set()
        while n != 1 and n not in nums:
            nums.add(n)
            n=getSum(n)
        
        return n == 1