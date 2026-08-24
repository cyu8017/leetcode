# LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
# https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        n, m = len(s), len(pattern)
        for i in range(n - m + 1):
            diff = 0
            for j in range(m):
                if s[i + j] != pattern[j]:
                    diff += 1
                    if diff > 1:
                        break
            if diff <= 1:
                return i
        return -1
