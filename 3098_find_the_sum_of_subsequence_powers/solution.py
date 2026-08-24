# LeetCode 3098 - Find the Sum of Subsequence Powers
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

from typing import List


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        nums = sorted(nums)
        n = len(nums)
        f = {}

        def dfs(i: int, j: int, kk: int, mi: int) -> int:
            if i >= n:
                return mi if kk == 0 else 0
            if n - i < kk:
                return 0
            key = (mi, i, j, kk)
            if key in f:
                return f[key]
            ans = dfs(i + 1, j, kk, mi)
            if j == n:
                ans = (ans + dfs(i + 1, i, kk - 1, mi)) % MOD
            else:
                ans = (ans + dfs(i + 1, i, kk - 1, min(mi, nums[i] - nums[j]))) % MOD
            f[key] = ans
            return ans

        return dfs(0, n, k, 10**18)
