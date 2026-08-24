# LeetCode 2741 - Special Permutations
# https://leetcode.com/problems/special-permutations/

from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 1000000007
        n = len(nums)
        memo = [[-1] * n for _ in range(1 << n)]

        def dfs(mask: int, last: int) -> int:
            if mask == (1 << n) - 1:
                return 1
            if memo[mask][last] != -1:
                return memo[mask][last]
            res = 0
            for i in range(n):
                if mask & (1 << i):
                    continue
                if nums[i] % nums[last] == 0 or nums[last] % nums[i] == 0:
                    res = (res + dfs(mask | (1 << i), i)) % MOD
            memo[mask][last] = res
            return res

        ans = 0
        for i in range(n):
            ans = (ans + dfs(1 << i, i)) % MOD
        return ans
