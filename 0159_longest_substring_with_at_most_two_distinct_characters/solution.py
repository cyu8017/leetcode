# LeetCode 0159 - Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counts: dict[str, int] = defaultdict(int)
        left = best = 0
        for right, char in enumerate(s):
            counts[char] += 1
            while len(counts) > 2:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            best = max(best, right - left + 1)
        return best
