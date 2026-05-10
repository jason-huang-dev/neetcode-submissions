class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result array 
        res = [1] * (len(nums))

        # obtain the prefix product of all elements to left of i
        # left to right
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        # obtain the postfix product of all elements to right of i
        # right to left
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        print(res)
        return res
        
        
        # Initial Solution that takes O(n^2) time and O(n) space
        # products = [1] * (len(nums))

        # for i, num in enumerate(nums):
        #     for j in range(0, len(products)):
        #         if j != i:
        #             products[j] *= num
                    
        # return products
