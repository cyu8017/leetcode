# LeetCode 3792 - Sum of Increasing Product Blocks
# https://leetcode.com/problems/sum-of-increasing-product-blocks/

class Solution:
    def sumOfBlocks(self, n: int) -> int:
        MOD = 1000000007
        ans = 0
        k = 1
        for i in range(1, n + 1):
            x = 1
            for j in range(k, k + i):
                x = x * j % MOD
            ans = (ans + x) % MOD
            k += i
        return ans
