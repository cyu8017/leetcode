# LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        prev = [-1] * n

        def hamming(a: str, b: str) -> int:
            if len(a) != len(b):
                return 100
            return sum(1 for i in range(len(a)) if a[i] != b[i])

        best = 1
        best_i = 0
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and hamming(words[i], words[j]) == 1 and dp[j] + 1 >= dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] >= best:
                best = dp[i]
                best_i = i
        path = []
        i = best_i
        while i != -1:
            path.append(words[i])
            i = prev[i]
        path.reverse()
        return path
