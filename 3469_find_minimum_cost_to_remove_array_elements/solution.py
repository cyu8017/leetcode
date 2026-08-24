# LeetCode 3469 - Find Minimum Cost to Remove Array Elements
# https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

from typing import List


class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def max2(a: int, b: int) -> int:
            return a if a > b else b

        def min3(a: int, b: int, c: int) -> int:
            return min(a, b, c)

        def key(i: int, prev: int) -> int:
            return (i << 32) | (prev & 0xFFFFFFFF)

        def dfs(i: int, prev: int) -> int:
            if i >= n:
                return 0 if prev == -1 else nums[prev]
            k = key(i, prev)
            if k in memo:
                return memo[k]
            if prev == -1:
                if i + 1 >= n:
                    res = nums[i]
                elif i + 2 >= n:
                    res = max2(nums[i], nums[i + 1])
                else:
                    a, b, c = nums[i], nums[i + 1], nums[i + 2]
                    res = min3(
                        max2(b, c) + dfs(i + 3, i),
                        max2(a, c) + dfs(i + 3, i + 1),
                        max2(a, b) + dfs(i + 3, i + 2),
                    )
            else:
                if i + 1 >= n:
                    res = max2(nums[prev], nums[i])
                else:
                    a, b, c = nums[prev], nums[i], nums[i + 1]
                    res = min3(
                        max2(b, c) + dfs(i + 2, prev),
                        max2(a, c) + dfs(i + 2, i),
                        max2(a, b) + dfs(i + 2, i + 1),
                    )
            memo[k] = res
            return res

        return dfs(0, -1)
