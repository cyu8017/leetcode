# LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt = {}
        n = len(word)
        mx = 0
        for i in range(0, n, k):
            s = word[i : i + k]
            v = cnt.get(s, 0) + 1
            cnt[s] = v
            mx = max(mx, v)
        return n // k - mx
