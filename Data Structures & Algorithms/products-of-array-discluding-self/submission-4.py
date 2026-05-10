class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * (len(nums))

        for i, num in enumerate(nums):
            for j in range(0, len(products)):
                if j != i:
                    products[j] *= num
                    
        return products
