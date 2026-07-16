# LeetCode 0940 - Distinct Subsequences II
# https://leetcode.com/problems/distinct-subsequences-ii/

from collections import defaultdict


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        ends: dict[str, int] = defaultdict(int)
        ends[""] = 1
        for ch in s:
            ends[ch] = sum(ends.values()) % MOD
        return (sum(ends.values()) - 1) % MOD
