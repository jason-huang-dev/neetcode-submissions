class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            dh = 0
            # increment left
            if leftMax <= rightMax:
                l += 1 
                dh = leftMax - height[l]
                leftMax = max(leftMax , height[l])                
                
            # decrement right
            else:
                r -= 1 
                dh = rightMax - height[r]
                rightMax = max(rightMax , height[r]) 
            res += max(0,dh)
        return res