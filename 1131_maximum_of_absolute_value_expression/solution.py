# LeetCode 1131 - Maximum of Absolute Value Expression
# https://leetcode.com/problems/maximum-of-absolute-value-expression/

class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        n = len(arr1)
        ans = 0
        for p, q in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            best = p * arr1[0] + q * arr2[0]
            for i in range(1, n):
                cur = p * arr1[i] + q * arr2[i] + i
                ans = max(ans, cur - best)
                best = min(best, p * arr1[i] + q * arr2[i] + i)
        return ans
