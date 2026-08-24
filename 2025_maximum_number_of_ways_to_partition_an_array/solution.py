# LeetCode 2025 - Maximum Number of Ways to Partition an Array
# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/

from typing import List


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * n
        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + nums[i]
        total = pref[n - 1]
        right, left = {}, {}
        for i in range(n - 1):
            right[pref[i]] = right.get(pref[i], 0) + 1
        ans = 0
        if total % 2 == 0:
            ans = right.get(total // 2, 0)
        for i in range(n):
            diff = k - nums[i]
            new_total = total + diff
            cur = 0
            if new_total % 2 == 0:
                half = new_total // 2
                cur = left.get(half, 0) + right.get(half - diff, 0)
            ans = max(ans, cur)
            if i < n - 1:
                left[pref[i]] = left.get(pref[i], 0) + 1
                right[pref[i]] -= 1
        return ans
