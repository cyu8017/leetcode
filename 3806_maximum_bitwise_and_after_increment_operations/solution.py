# LeetCode 3806 - Maximum Bitwise AND After Increment Operations
# https://leetcode.com/problems/maximum-bitwise-and-after-increment-operations/

from typing import List


class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        def BitLen(x: int) -> int:
            if x == 0:
                return 0
            n = 0
            while x > 0:
                n += 1
                x >>= 1
            return n

        mxVal = nums[0]
        for v in nums:
            if v > mxVal:
                mxVal = v
        mxVal += k
        mx = BitLen(mxVal)
        ans = 0
        cost = [0] * len(nums)
        for bit in range(mx - 1, -1, -1):
            target = ans | (1 << bit)
            for i, x in enumerate(nums):
                j = BitLen(target & ~x)
                mask = (1 << j) - 1
                cost[i] = (target & mask) - (x & mask)
            cost.sort()
            total = 0
            for i in range(m):
                total += cost[i]
            if total <= k:
                ans = target
        return ans
