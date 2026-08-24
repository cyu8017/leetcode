# LeetCode 3575 - Maximum Good Subtree Score
# https://leetcode.com/problems/maximum-good-subtree-score/

from typing import Dict, List, Tuple


class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        MOD = 1000000007
        n = len(vals)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[par[i]].append(i)
        ans = 0

        def digit_mask(x: int) -> Tuple[int, int, int]:
            v = x
            mask = 0
            if x == 0:
                return (1, 1, 0)
            while x > 0:
                d = x % 10
                if (mask & (1 << d)) != 0:
                    return (0, 0, 0)
                mask |= 1 << d
                x //= 10
            return (mask, 1, v)

        def dfs(u: int) -> Dict[int, int]:
            nonlocal ans
            dp = {0: 0}
            dm = digit_mask(vals[u])
            if dm[1] == 1:
                dp[dm[0]] = dm[2]
            for c in g[u]:
                child = dfs(c)
                ndp = {}
                for k1, v1 in dp.items():
                    for k2, v2 in child.items():
                        if (k1 & k2) == 0:
                            nm = k1 | k2
                            ndp[nm] = max(ndp.get(nm, 0), v1 + v2)
                for k, v in dp.items():
                    ndp[k] = max(ndp.get(k, 0), v)
                for k, v in child.items():
                    ndp[k] = max(ndp.get(k, 0), v)
                dp = ndp
            best = 0
            for s in dp.values():
                best = max(best, s)
            ans = (ans + best) % MOD
            return dp

        dfs(0)
        return ans
