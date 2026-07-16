# LeetCode 0383 - Ransom Note
# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for char in ransomNote:
            if counts[char] == 0:
                return False
            counts[char] -= 1
        return True
