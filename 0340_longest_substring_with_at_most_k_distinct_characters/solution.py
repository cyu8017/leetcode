# LeetCode 0340 - Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        counts: dict[str, int] = defaultdict(int)
        left = 0
        best = 0

        for right, char in enumerate(s):
            counts[char] += 1
            while len(counts) > k:
                left_char = s[left]
                counts[left_char] -= 1
                if counts[left_char] == 0:
                    del counts[left_char]
                left += 1
            best = max(best, right - left + 1)

        return best
