# LeetCode 0885 - Spiral Matrix III
# https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        ans = [[rStart, cStart]]
        if rows * cols == 1:
            return ans
        r, c = rStart, cStart
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = 1
        while len(ans) < rows * cols:
            for d in range(4):
                dr, dc = dirs[d]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        ans.append([r, c])
                        if len(ans) == rows * cols:
                            return ans
                if d % 2 == 1:
                    steps += 1
        return ans
