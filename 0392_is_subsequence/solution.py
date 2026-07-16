# LeetCode 0392 - Is Subsequence
# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for char in t:
            if index < len(s) and s[index] == char:
                index += 1
        return index == len(s)
