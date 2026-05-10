class Solution:
    def search(self, nums: List[int], target: int) -> int:
        h,l = len(nums)-1, 0

        while h >= l:
            mid = l + (h-l)//2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                h = mid -1
        
        return -1