# LeetCode 2573 - Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/

from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [0] * n
        c = 97
        for i in range(n):
            if s[i] != 0:
                continue
            if c > 122:
                return ""
            s[i] = c
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    s[j] = c
            c += 1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                v = 0
                if s[i] == s[j]:
                    v = 1
                    if i + 1 < n and j + 1 < n:
                        v += lcp[i + 1][j + 1]
                if lcp[i][j] != v:
                    return ""
        return "".join(chr(x) for x in s)
