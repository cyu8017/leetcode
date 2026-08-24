# LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for x in nums:
            max_or |= x
        ans = 0

        def dfs(i: int, cur: int) -> None:
            nonlocal ans
            if i == len(nums):
                if cur == max_or:
                    ans += 1
                return
            dfs(i + 1, cur)
            dfs(i + 1, cur | nums[i])

        dfs(0, 0)
        return ans
