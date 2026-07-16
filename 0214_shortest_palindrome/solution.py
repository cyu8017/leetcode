# LeetCode 0214 - Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        combined = s + "#" + s[::-1]
        lps = 0
        pi = [0] * len(combined)
        for i in range(1, len(combined)):
            while lps and combined[i] != combined[lps]:
                lps = pi[lps - 1]
            if combined[i] == combined[lps]:
                lps += 1
            pi[i] = lps
        prefix_len = pi[-1]
        return s[prefix_len:][::-1] + s
