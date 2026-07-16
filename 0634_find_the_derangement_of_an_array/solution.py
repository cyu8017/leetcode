# LeetCode 0634 - Find the Derangement of An Array
# https://leetcode.com/problems/find-the-derangement-of-an-array/


class Solution:
    def findDerangement(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 0
        prev2, prev1 = 0, 1
        for size in range(3, n + 1):
            prev2, prev1 = prev1, (size - 1) * (prev1 + prev2) % mod
        return prev1 if n > 1 else 0
