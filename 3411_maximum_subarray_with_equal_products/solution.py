# LeetCode 3411 - Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/

from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 1
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                if prod > 1000000000 // nums[j]:
                    break
                prod *= nums[j]
                if g == 0:
                    g = nums[j]
                    l = nums[j]
                else:
                    g = gcd(g, nums[j])
                    l = l // gcd(l, nums[j]) * nums[j]
                if prod == l * g and j - i + 1 > ans:
                    ans = j - i + 1
        return ans
