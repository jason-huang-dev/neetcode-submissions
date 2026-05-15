class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nesw = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(x:int,y:int):
            if x < 0 or x >= len(grid) or  y < 0 or y >= len(grid[0]) or grid[x][y]=="0":
                return

            grid[x][y] = "0"

            for dx,dy in nesw:
                nx = x + dx
                ny = y + dy
                dfs(nx,ny)



        islands = 0
        for i,row in enumerate(grid):
            for j, col in enumerate(row):
                if "1"==grid[i][j]:
                    islands += 1
                    dfs(i,j)
        return islands