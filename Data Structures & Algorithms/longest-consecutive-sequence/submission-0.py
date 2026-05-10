from collections import defaultdict

"""
Create map to store num:max legth
length of num = num-1 + num+1
But we need to update the head and tail of the sequence so they hold the proper value
Duplicates should be skipped
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        mp = defaultdict(int)
        res = 0

        for num in nums:
            if mp[num]:
                continue

            # Calculates the length of this sequence
            mp[num] = mp[num-1]+mp[num+1]+1

            # find the start of this sequence and update its length
            mp[num-mp[num-1]] = mp[num]
            # find the end of this sequence and update its length
            mp[num+mp[num+1]] = mp[num]
            res = max(res, mp[num])
        return res


