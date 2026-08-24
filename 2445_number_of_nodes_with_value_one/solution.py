# LeetCode 2445 - Number of Nodes With Value One
# https://leetcode.com/problems/number-of-nodes-with-value-one/

from typing import List


class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        flip = [0] * (n + 1)
        val = [0] * (n + 1)
        for q in queries:
            flip[q] ^= 1
        ans = 0
        for i in range(1, n + 1):
            val[i] = flip[i]
            if i > 1:
                val[i] ^= val[i // 2]
            ans += val[i]
        return ans
