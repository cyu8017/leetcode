# LeetCode 1876 - Substrings of Size Three with Distinct Characters
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0
        for i in range(len(s) - 2):
            window = s[i : i + 3]
            if len(set(window)) == 3:
                count += 1
        return count
