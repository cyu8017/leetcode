# LeetCode 3696 - Maximum Distance Between Unequal Words in Array I
# https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-i/

from typing import List


class Solution:
    def maxDistance(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            if words[i] != words[0]:
                ans = max(ans, i + 1)
            if words[i] != words[n - 1]:
                ans = max(ans, n - i)
        return ans
