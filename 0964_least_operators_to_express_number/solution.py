# LeetCode 0964 - Least Operators to Express Number
# https://leetcode.com/problems/least-operators-to-express-number/

from functools import lru_cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        @lru_cache(None)
        def dfs(t: int) -> int:
            if x > t:
                return min(2 * t - 1, 2 * (x - t))
            if x == t:
                return 0
            prod = x
            n = 0
            while prod < t:
                prod *= x
                n += 1
            if prod == t:
                return n
            ans = dfs(t - prod // x) + n
            if prod < 2 * t:
                ans = min(ans, dfs(prod - t) + n + 1)
            return ans

        return dfs(target)
