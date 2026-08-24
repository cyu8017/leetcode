# LeetCode 2261 - K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/

from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        seen = set()
        for i in range(n):
            div = 0
            key = ""
            for j in range(i, n):
                if nums[j] % p == 0:
                    div += 1
                if div > k:
                    break
                key += str(nums[j] + 1) + ","
                seen.add(key)
        return len(seen)
