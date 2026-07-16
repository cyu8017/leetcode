# LeetCode 0132 - Palindrome Partitioning II
# https://leetcode.com/problems/palindrome-partitioning-ii/


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        cuts = list(range(n))
        for i in range(n):
            if is_pal[0][i]:
                cuts[i] = 0
                continue
            for j in range(i):
                if is_pal[j + 1][i]:
                    cuts[i] = min(cuts[i], cuts[j] + 1)
        return cuts[-1]
