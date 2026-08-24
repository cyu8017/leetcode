# LeetCode 3571 - Find the Shortest Superstring II
# https://leetcode.com/problems/find-the-shortest-superstring-ii/


class Solution:
    def shortestSuperstring(self, s1: str, s2: str) -> str:
        if len(s1) > len(s2):
            return self.shortestSuperstring(s2, s1)
        m = len(s1)
        if s1 in s2:
            return s2
        for i in range(m):
            if s2.startswith(s1[i:]):
                return s1[:i] + s2
            length = m - i
            if len(s2) >= length and s2[-length:] == s1[:length]:
                return s2 + s1[m - i :]
        return s1 + s2
