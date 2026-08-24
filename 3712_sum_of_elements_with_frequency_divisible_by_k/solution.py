# LeetCode 3712 - Sum of Elements With Frequency Divisible by K
# https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

from typing import List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        cnt = {}
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
        ans = 0
        for key, val in cnt.items():
            if val % k == 0:
                ans += key * val
        return ans
