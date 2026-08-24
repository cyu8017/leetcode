# LeetCode 3149 - Find the Minimum Cost Array Permutation
# https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

from typing import List


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        memo = [[-1] * n for _ in range(1 << n)]

        def absv(x: int) -> int:
            return -x if x < 0 else x

        def dfs(mask: int, pre: int) -> int:
            if mask == (1 << n) - 1:
                return absv(pre - nums[0])
            if memo[mask][pre] != -1:
                return memo[mask][pre]
            res = 10**18
            for cur in range(1, n):
                if ((mask >> cur) & 1) == 0:
                    res = min(res, absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur))
            memo[mask][pre] = res
            return res

        ans = []

        def g(mask: int, pre: int) -> None:
            ans.append(pre)
            if mask == (1 << n) - 1:
                return
            res = dfs(mask, pre)
            for cur in range(1, n):
                if ((mask >> cur) & 1) == 0:
                    if absv(pre - nums[cur]) + dfs(mask | (1 << cur), cur) == res:
                        g(mask | (1 << cur), cur)
                        break

        g(1, 0)
        return ans
