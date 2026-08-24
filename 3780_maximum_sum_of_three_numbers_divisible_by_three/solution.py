# LeetCode 3780 - Maximum Sum of Three Numbers Divisible by Three
# https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        a = sorted(nums)
        g = [[], [], []]
        for x in a:
            g[x % 3].append(x)
        ans = 0
        for aa in range(3):
            if g[aa]:
                x = g[aa].pop()
                for b in range(3):
                    if g[b]:
                        y = g[b].pop()
                        c = (3 - (aa + b) % 3) % 3
                        if g[c]:
                            z = g[c][-1]
                            ans = max(ans, x + y + z)
                        g[b].append(y)
                g[aa].append(x)
        return ans
