# LeetCode 3503 - Longest Palindrome After Substring Concatenation I
# https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/

from typing import List


class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def expand(st: str, g: List[int], l: int, r: int) -> None:
            while l >= 0 and r < len(st) and st[l] == st[r]:
                g[l] = max(g[l], r - l + 1)
                l -= 1
                r += 1

        def calc(st: str) -> List[int]:
            n = len(st)
            g = [0] * n
            for i in range(n):
                expand(st, g, i, i)
                expand(st, g, i, i + 1)
            return g

        m, n = len(s), len(t)
        t = t[::-1]
        g1, g2 = calc(s), calc(t)
        ans = 0
        for v in g1:
            ans = max(ans, v)
        for v in g2:
            ans = max(ans, v)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                    a = g1[i] if i < m else 0
                    b = g2[j] if j < n else 0
                    ans = max(ans, f[i][j] * 2 + a)
                    ans = max(ans, f[i][j] * 2 + b)
        return ans
