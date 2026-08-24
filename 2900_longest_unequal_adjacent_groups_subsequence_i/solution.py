# LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        last = groups[0]
        for i in range(1, len(words)):
            if groups[i] != last:
                ans.append(words[i])
                last = groups[i]
        return ans
