# LeetCode 2672 - Number of Adjacent Elements With the Same Color
# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        ans = [0] * len(queries)
        same = 0
        for i, (idx, color) in enumerate(queries):
            if colors[idx] != 0:
                if idx > 0 and colors[idx] == colors[idx - 1]:
                    same -= 1
                if idx + 1 < n and colors[idx] == colors[idx + 1]:
                    same -= 1
            colors[idx] = color
            if idx > 0 and colors[idx] == colors[idx - 1]:
                same += 1
            if idx + 1 < n and colors[idx] == colors[idx + 1]:
                same += 1
            ans[i] = same
        return ans
