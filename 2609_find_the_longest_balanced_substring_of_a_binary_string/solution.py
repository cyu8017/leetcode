# LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        zeros = 0
        ones = 0
        for c in s:
            if c == "0":
                if ones > 0:
                    zeros = ones = 0
                zeros += 1
            else:
                ones += 1
                cur = min(ones, zeros)
                if 2 * cur > ans:
                    ans = 2 * cur
        return ans
