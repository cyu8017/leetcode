# LeetCode 0567 - Permutation in String
# https://leetcode.com/problems/permutation-in-string/

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = len(s1)
        if need > len(s2):
            return False

        target = Counter(s1)
        window: Counter[str] = Counter()
        left = 0

        for right, char in enumerate(s2):
            window[char] += 1
            while right - left + 1 > need:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if window == target:
                return True

        return False
