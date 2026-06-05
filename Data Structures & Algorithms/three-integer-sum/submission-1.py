class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        n = len(nums)
        d = collections.defaultdict(set)
        res = set()

        for i in range(n):
            for j in range(i+1, n):
                s = nums[i] + nums[j]
                if -nums[j] in d:
                    for x,y,index in d[-nums[j]]:
                        if j != index:
                            res.add(tuple(sorted([nums[j],x,y])))
            
                d[s].add((nums[i], nums[j], j))

        return [list(x) for x in res]
