class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1

        res = 0
        while l < r:
            width = r-l
            height = min(heights[l], heights[r])

            res = max(res,width*height)

            #if left height is less than right move 
            if heights[l] <= heights[r]:
                l += 1

            # else move the left
            else:
                r -=1
        return res