# LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
# https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def square_free(x: int) -> int:
            res = 1
            p = 2
            while p * p <= x:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                if cnt % 2 == 1:
                    res *= p
                p += 1
            if x > 1:
                res *= x
            return res

        n = len(nums)
        groups = {}
        ans = 0
        for i in range(1, n + 1):
            sf = square_free(i)
            s = groups.get(sf, 0) + nums[i - 1]
            groups[sf] = s
            if s > ans:
                ans = s
        return ans
