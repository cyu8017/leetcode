# LeetCode 3995 - Minimum Cost to Convert String III
# https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

from typing import List


class Solution:
    def minCost(self, source: str, target: str, rules: List[List[str]], costs: List[int]) -> int:
        n = len(source)
        if len(target) != n:
            return -1
        dp = [2147483647] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == 2147483647:
                continue
            if source[i] == target[i] and dp[i] < dp[i + 1]:
                dp[i + 1] = dp[i]
            for j in range(len(rules)):
                p = rules[j][0]
                r = rules[j][1]
                plen = len(p)
                if i + plen > n:
                    continue
                c = costs[j]
                ok = True
                for k in range(plen):
                    if r[k] != target[i + k]:
                        ok = False
                        break
                    if p[k] == "*":
                        c += 1
                    elif p[k] != source[i + k]:
                        ok = False
                        break
                if ok and dp[i] <= 2147483647 - c and dp[i] + c < dp[i + plen]:
                    dp[i + plen] = dp[i] + c
        return -1 if dp[n] == 2147483647 else dp[n]
