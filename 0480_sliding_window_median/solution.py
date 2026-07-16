# LeetCode 0480 - Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/

import bisect


class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        window = sorted(nums[:k])
        result: list[float] = []

        def append_median() -> None:
            if k % 2:
                result.append(float(window[k // 2]))
            else:
                result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

        append_median()
        for index in range(k, len(nums)):
            outgoing = nums[index - k]
            incoming = nums[index]
            window.pop(bisect.bisect_left(window, outgoing))
            bisect.insort(window, incoming)
            append_median()
        return result
