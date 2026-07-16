# LeetCode 1347 - Minimum Number Of Steps To Make Two Strings Anagram

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        difference = Counter(s) - Counter(t)
        return sum(difference.values())
