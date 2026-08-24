# LeetCode 3850 - Count Sequences To K
# https://leetcode.com/problems/count-sequences-to-k/

from typing import Dict, List


class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        f: Dict[str, int] = {}

        def dfs(i: int, p: int, q: int) -> int:
            if i == len(nums):
                return 1 if p == k and q == 1 else 0
            key = f"{i},{p},{q}"
            if key in f:
                return f[key]
            res = dfs(i + 1, p, q)
            x = nums[i]
            g1 = gcd(p * x, q)
            res += dfs(i + 1, (p * x) // g1, q // g1)
            g2 = gcd(p, q * x)
            res += dfs(i + 1, p // g2, (q * x) // g2)
            f[key] = res
            return res

        return dfs(0, 1, 1)
