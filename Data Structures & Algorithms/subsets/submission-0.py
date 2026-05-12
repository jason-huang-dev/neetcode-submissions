class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for n in nums:
            cur_set = []
            for sets in subsets:
                cur_set.append(list(sets) + [n])
            subsets = subsets + cur_set
        return subsets