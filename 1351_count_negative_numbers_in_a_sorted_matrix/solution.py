class Solution:
    def countNegatives(self, grid):
        return sum(len(row) - next((i for i, x in enumerate(row) if x < 0), len(row)) for row in grid)
