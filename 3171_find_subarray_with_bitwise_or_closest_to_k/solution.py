# LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
# https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

from typing import List


def leading_zero_count(x: int) -> int:
    if x == 0:
        return 32
    n = 0
    for bit in range(31, -1, -1):
        if ((x >> bit) & 1) != 0:
            break
        n += 1
    return n


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        mx = 0
        for v in nums:
            mx = max(mx, v)
        m = 1 if mx == 0 else 32 - leading_zero_count(mx)
        cnt = [0] * m
        ans = 10**18
        s = 0
        i = 0
        for j, x in enumerate(nums):
            s |= x
            ans = min(ans, abs(s - k))
            for h in range(m):
                if ((x >> h) & 1) != 0:
                    cnt[h] += 1
            while i < j and s > k:
                y = nums[i]
                for h in range(m):
                    if ((y >> h) & 1) != 0:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h
                ans = min(ans, abs(s - k))
                i += 1
        return ans
