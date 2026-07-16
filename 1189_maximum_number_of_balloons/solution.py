# LeetCode 1189 - Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])
