# LeetCode 3127 - Make a Square with the Same Color
# https://leetcode.com/problems/make-a-square-with-the-same-color/

from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        dirs = [0, 0, 1, 1, 0]
        for i in range(2):
            for j in range(2):
                cnt1 = 0
                cnt2 = 0
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if grid[x][y] == "W":
                        cnt1 += 1
                    else:
                        cnt2 += 1
                if cnt1 != cnt2:
                    return True
        return False
