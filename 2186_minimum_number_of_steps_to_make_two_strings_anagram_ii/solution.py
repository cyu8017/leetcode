# LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq = [0] * (26)
        for i in range(len(s)):
            freq[ord(s[i]) - 97] += 1
        for i in range(len(t)):
            freq[ord(t[i]) - 97] -= 1
        ans = 0
        for v in freq:
            ans += abs(v)
        return ans
