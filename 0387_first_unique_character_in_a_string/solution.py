# LeetCode 0387 - First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for index, char in enumerate(s):
            if counts[char] == 1:
                return index
        return -1
