
class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0
        def explore_island(row, col):
            stack = [(row, col)]  
            while stack:
                r, c = stack.pop()
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'W':
                    continue
                grid[r][c] = 'W'
                stack.append((r - 1, c))  
                stack.append((r + 1, c))  
                stack.append((r, c - 1))  
                stack.append((r, c + 1)) 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'L':
                    explore_island(row, col) 
                    res += 1 

        return res

