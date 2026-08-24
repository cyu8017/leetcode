# LeetCode 3334 - Find the Maximum Factor Score of Array
# https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

from typing import List


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcd_all = nums[0]
        lcm_all = nums[0]
        for i in range(1, n):
            gcd_all = gcd(gcd_all, nums[i])
            lcm_all = lcm(lcm_all, nums[i])
        ans = gcd_all * lcm_all
        for skip in range(n):
            g = 0
            l = 1
            first = True
            for i in range(n):
                if i == skip:
                    continue
                if first:
                    g = l = nums[i]
                    first = False
                else:
                    g = gcd(g, nums[i])
                    l = lcm(l, nums[i])
            if first:
                continue
            v = g * l
            if v > ans:
                ans = v
        return ans
