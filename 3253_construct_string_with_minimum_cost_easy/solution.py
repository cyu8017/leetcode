# LeetCode 3253 - Construct String with Minimum Cost (Easy)
# https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

from typing import Dict, List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        inf = 10**18
        n = len(target)
        dp = [inf] * (n + 1)
        dp[0] = 0
        best: Dict[str, int] = {}
        for i in range(len(words)):
            old = best.get(words[i])
            if old is None or costs[i] < old:
                best[words[i]] = costs[i]
        for i in range(n):
            if dp[i] == inf:
                continue
            for w, c in best.items():
                L = len(w)
                if i + L <= n and target.startswith(w, i) and dp[i] + c < dp[i + L]:
                    dp[i + L] = dp[i] + c
        if dp[n] == inf:
            return -1
        return dp[n]
