# LeetCode 3097 - Shortest Subarray With OR at Least K II
# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = [0] * 32
        ans = n + 1
        s = 0
        i = 0
        for j in range(n):
            x = nums[j]
            s |= x
            for h in range(32):
                if ((x >> h) & 1) != 0:
                    cnt[h] += 1
            while s >= k and i <= j:
                ans = min(ans, j - i + 1)
                for h in range(32):
                    if ((nums[i] >> h) & 1) != 0:
                        cnt[h] -= 1
                        if cnt[h] == 0:
                            s ^= 1 << h
                i += 1
        return -1 if ans == n + 1 else ans
