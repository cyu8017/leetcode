# LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

from typing import List


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        MIN = -5000
        memo = {}
        sum_all = 0
        for v in nums:
            sum_all += v
        if abs(k) > sum_all:
            return -1

        def dp(i: int, product: int, state: int, kk: int) -> int:
            if i == len(nums):
                if kk == 0 and state != 0 and product <= limit:
                    return product
                return MIN
            key = (i, product, state, kk)
            if key in memo:
                return memo[key]
            res = dp(i + 1, product, state, kk)
            if state == 0:
                res = max(res, dp(i + 1, nums[i], 1, kk - nums[i]))
            if state == 1:
                np = product * nums[i]
                if np > limit + 1:
                    np = limit + 1
                res = max(res, dp(i + 1, np, 2, kk + nums[i]))
            if state == 2:
                np = product * nums[i]
                if np > limit + 1:
                    np = limit + 1
                res = max(res, dp(i + 1, np, 1, kk - nums[i]))
            memo[key] = res
            return res

        ans = dp(0, 1, 0, k)
        return -1 if ans == MIN else ans
