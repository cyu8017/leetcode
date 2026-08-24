# LeetCode 3867 - Sum Of Gcd Of Formed Pairs
# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

from typing import List


class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a

        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            prefix_gcd[i] = gcd(nums[i], mx)
        prefix_gcd.sort()
        ans = 0
        for i in range(n // 2):
            ans += gcd(prefix_gcd[i], prefix_gcd[n - i - 1])
        return ans
