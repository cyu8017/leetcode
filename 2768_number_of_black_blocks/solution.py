# LeetCode 2768 - Number of Black Blocks
# https://leetcode.com/problems/number-of-black-blocks/

from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        cnt = {}
        for x, y in coordinates:
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    if 0 <= i < m - 1 and 0 <= j < n - 1:
                        key = (i, j)
                        cnt[key] = cnt.get(key, 0) + 1
        out = [0] * 5
        out[0] = (m - 1) * (n - 1)
        for v in cnt.values():
            out[v] += 1
            out[0] -= 1
        return out
