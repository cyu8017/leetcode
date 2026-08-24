# LeetCode 3499 - Maximize Active Section with Trade I
# https://leetcode.com/problems/maximize-active-section-with-trade-i/


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = 0
        for c in s:
            if c == "1":
                ones += 1
        zeros = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] != "0":
                i += 1
                continue
            j = i
            while j < n and s[j] == "0":
                j += 1
            zeros.append((i, j - 1))
            i = j
        best = 0
        for i in range(len(zeros) - 1):
            gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1)
            if gain > best:
                best = gain
        return ones + best
