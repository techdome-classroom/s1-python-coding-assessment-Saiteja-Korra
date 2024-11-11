# class Solution:
   
#     def getTotalIsles(self, grid: list[list[str]]) -> int:
#     #    write your code here
#         if not grid:
#             return 0

#         def dfs(r, c):
#             if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'W':
#                 return 
#             grid[r][c] = 'W'
#             dfs(r - 1, c)
#             dfs(r + 1, c)
#             dfs(r, c - 1)
#             dfs(r, c + 1)
#         res = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == 'L':
#                     dfs(r, c)
#                     res += 1
        
                  
#         return res

class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        island_count = 0
        def explore_island(row, col):
            stack = [(row, col)]  
            while stack:
                r, c = stack.pop()
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 'W':
                    continue
                # Mark the cell as visited by changing 'L' to 'W'
                grid[r][c] = 'W'
                # Add neighboring cells to the stack for exploration
                stack.append((r - 1, c))  # up
                stack.append((r + 1, c))  # down
                stack.append((r, c - 1))  # left
                stack.append((r, c + 1))  # right

        # Iterate over each cell in the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Start a new island exploration if an unvisited land cell is found
                if grid[row][col] == 'L':
                    explore_island(row, col)  # Mark the entire island as visited
                    island_count += 1  # Increment the island counter

        return island_count

