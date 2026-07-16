# LeetCode 0438 - Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        need = [0] * 26
        window = [0] * 26
        for char in p:
            need[ord(char) - ord("a")] += 1

        result: list[int] = []
        left = 0
        for right, char in enumerate(s):
            window[ord(char) - ord("a")] += 1
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord("a")] -= 1
                left += 1
            if window == need:
                result.append(left)
        return result
