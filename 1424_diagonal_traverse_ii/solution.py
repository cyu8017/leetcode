class Solution:
    def findDiagonalOrder(self, nums):
        diagonals = {}
        for row, values in enumerate(nums):
            for col, value in enumerate(values):
                diagonals.setdefault(row + col, []).append(value)
        return [value for key in sorted(diagonals) for value in reversed(diagonals[key])]
