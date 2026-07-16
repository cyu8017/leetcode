# LeetCode 1147 - Longest Chunked Palindrome Decomposition
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        ans = 0
        i = 0
        while i < n - i:
            found = False
            for length in range(1, (n - 2 * i) // 2 + 1):
                if text[i : i + length] == text[n - i - length : n - i]:
                    ans += 2
                    i += length
                    found = True
                    break
            if not found:
                ans += 1
                break
        return ans
