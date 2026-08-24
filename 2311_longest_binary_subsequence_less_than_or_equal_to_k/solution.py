# LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = s.count("0")
        val = ones = 0
        pow2 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                if not (pow2 > k or val + pow2 > k):
                    val += pow2
                    ones += 1
            if pow2 <= k:
                pow2 *= 2
        return zeros + ones
