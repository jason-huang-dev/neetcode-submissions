import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # At any point we have two options
        # Option 1: Pick up the number and add it to the sub array
        # Option 2: Start the subarray at the current index and store the max
        res = nums[0]
        glob = nums[0]
        for num in nums[1:]:
            res = max(num, res + num)
            glob = max(res, glob)
        return glob

