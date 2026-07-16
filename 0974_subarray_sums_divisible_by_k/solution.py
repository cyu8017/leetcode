# LeetCode 0974 - Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k/

from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix = ans = 0
        for x in nums:
            prefix = (prefix + x) % k
            ans += count[prefix]
            count[prefix] += 1
        return ans
