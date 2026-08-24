# LeetCode 2964 - Number of Divisible Triplet Sums
# https://leetcode.com/problems/number-of-divisible-triplet-sums/

from typing import List


class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            freq = {}
            for j in range(i + 1, n):
                need = (d - (nums[i] + nums[j]) % d) % d
                ans += freq.get(need, 0)
                key = nums[j] % d
                freq[key] = freq.get(key, 0) + 1
        return ans
