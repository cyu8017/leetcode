# LeetCode 0727 - Minimum Window Subsequence
# https://leetcode.com/problems/minimum-window-subsequence/


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        best = ""
        i = 0
        while i < m:
            j = 0
            k = i
            while k < m and j < n:
                if s1[k] == s2[j]:
                    j += 1
                k += 1
            if j < n:
                break

            end = k - 1
            j = n - 1
            k = end
            while j >= 0:
                if s1[k] == s2[j]:
                    j -= 1
                k -= 1
            start = k + 1
            if not best or end - start + 1 < len(best):
                best = s1[start : end + 1]
            i = start + 1
        return best
