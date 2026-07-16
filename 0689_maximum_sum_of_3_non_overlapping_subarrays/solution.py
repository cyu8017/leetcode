# LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        windows = n - k + 1
        sums = [0] * windows
        total = sum(nums[:k])
        sums[0] = total
        for i in range(1, windows):
            total += nums[i + k - 1] - nums[i - 1]
            sums[i] = total

        left = [0] * windows
        best = 0
        for i in range(windows):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        right = [0] * windows
        best = windows - 1
        for i in range(windows - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        answer = [0, 0, 0]
        best_total = -1
        for mid in range(k, windows - k):
            l, r = left[mid - k], right[mid + k]
            total = sums[l] + sums[mid] + sums[r]
            if total > best_total:
                best_total = total
                answer = [l, mid, r]
        return answer
