# LeetCode 3864 - Minimum Cost To Partition A Binary String
# https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/


class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + (ord(s[i - 1]) - 48)

        def dfs(l: int, r: int) -> int:
            x = pre[r] - pre[l]
            res = (r - l) * x * encCost if x != 0 else flatCost
            if (r - l) % 2 == 0:
                m = (l + r) // 2
                res = min(res, dfs(l, m) + dfs(m, r))
            return res

        return dfs(0, n)
