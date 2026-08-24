# LeetCode 3146 - Permutation Difference between Two Strings
# https://leetcode.com/problems/permutation-difference-between-two-strings/


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d = [0] * 26
        for i, ch in enumerate(s):
            d[ord(ch) - 97] = i
        ans = 0
        for i, ch in enumerate(t):
            ans += abs(d[ord(ch) - 97] - i)
        return ans
