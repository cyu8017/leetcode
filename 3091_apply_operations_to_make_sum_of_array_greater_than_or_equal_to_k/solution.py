# LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
# https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/


class Solution:
    def minOperations(self, k: int) -> int:
        ans = k
        for a in range(k):
            x = a + 1
            b = (k + x - 1) // x - 1
            ans = min(ans, a + b)
        return ans
