# LeetCode 0424 - Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts: dict[str, int] = {}
        left = 0
        best = 0
        max_count = 0

        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            max_count = max(max_count, counts[char])
            while (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return best
