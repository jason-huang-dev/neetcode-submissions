import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        counts = collections.Counter(nums)
        most_frequent = counts.most_common(k)
        return [x for x,_ in most_frequent]