# LeetCode 1881 - Maximum Value after Insertion
# https://leetcode.com/problems/maximum-value-after-insertion/


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        neg = n[0] == "-"
        start = 1 if neg else 0
        for i in range(start, len(n)):
            d = int(n[i])
            if neg:
                if d > x:
                    return n[:i] + str(x) + n[i:]
            elif d < x:
                return n[:i] + str(x) + n[i:]
        return n + str(x)
