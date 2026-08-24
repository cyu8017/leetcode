# LeetCode 2450 - Number of Distinct Binary Strings After Applying Operations
# https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/


class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        mod = 1000000007
        n = len(s)
        ans = 1
        for _ in range(n - k + 1):
            ans = (ans * 2) % mod
        return ans
