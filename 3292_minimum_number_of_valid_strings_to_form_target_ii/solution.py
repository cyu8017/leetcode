# LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

from typing import List


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        inf = 1000000000
        dp = [inf] * (n + 1)
        dp[0] = 0
        root = {"next": [None] * 26}
        for w in words:
            cur = root
            for c in w:
                ci = ord(c) - 97
                if not cur["next"][ci]:
                    cur["next"][ci] = {"next": [None] * 26}
                cur = cur["next"][ci]
        for i in range(n):
            if dp[i] == inf:
                continue
            cur = root
            for j in range(i, n):
                ci = ord(target[j]) - 97
                if not cur["next"][ci]:
                    break
                cur = cur["next"][ci]
                if dp[i] + 1 < dp[j + 1]:
                    dp[j + 1] = dp[i] + 1
        return -1 if dp[n] == inf else dp[n]
