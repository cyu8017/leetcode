# LeetCode 2875 - Minimum Size Subarray in Infinite Array
# https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        ans = 1 << 30
        if total > 0:
            loops = target // total
            remain = target % total
            if remain == 0:
                return loops * n
            arr = nums + nums
            left = 0
            s = 0
            best = 1 << 30
            for right in range(len(arr)):
                s += arr[right]
                while s > remain and left <= right:
                    s -= arr[left]
                    left += 1
                if s == remain and right - left + 1 < best:
                    best = right - left + 1
            if best < (1 << 30):
                ans = loops * n + best
        return -1 if ans == (1 << 30) else ans
