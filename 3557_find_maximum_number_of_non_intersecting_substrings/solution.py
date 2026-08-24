# LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/


class Solution:
    def maxSubstrings(self, word: str) -> int:
        ans = 0
        first = {}
        for i, c in enumerate(word):
            if c not in first:
                first[c] = i
            elif i - first[c] + 1 >= 4:
                ans += 1
                first.clear()
        return ans
