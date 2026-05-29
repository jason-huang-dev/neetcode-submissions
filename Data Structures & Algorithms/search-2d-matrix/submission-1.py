class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        l,h = 0,n-1
        row = 0
        while h >= l:
            mid = l + (h-l)//2

            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                row = mid
                break
            elif target > matrix[mid][-1]:
                l = mid+1
            else:
                h = mid-1
        
        
        l,h = 0,m-1
        while h >= l:
            mid = l + (h-l)//2
            if target == matrix[row][mid]:
                return True
            elif target > matrix[row][mid]:
                l = mid+1
            else:
                h = mid-1

        return False