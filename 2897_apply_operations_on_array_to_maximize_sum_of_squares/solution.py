# LeetCode 2897 - Apply Operations on Array to Maximize Sum of Squares
# https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/

from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        cnt = [0] * 32
        for v in nums:
            for b in range(32):
                if (v & (1 << b)) != 0:
                    cnt[b] += 1
        ans = 0
        for _ in range(k):
            cur = 0
            for b in range(32):
                if cnt[b] > 0:
                    cur |= 1 << b
                    cnt[b] -= 1
            ans = (ans + ((cur % mod) * (cur % mod)) % mod) % mod
        return ans
