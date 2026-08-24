# LeetCode 3417 - Zigzag Grid Traversal With Skip
# https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

from typing import List


class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        skip = False
        for i, row in enumerate(grid):
            if i % 2 == 0:
                for v in row:
                    if not skip:
                        ans.append(v)
                    skip = not skip
            else:
                for j in range(len(row) - 1, -1, -1):
                    if not skip:
                        ans.append(row[j])
                    skip = not skip
        return ans
