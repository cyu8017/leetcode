# LeetCode 0239 - Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window: deque[int] = deque()
        result: list[int] = []
        for index, num in enumerate(nums):
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(index)
            if window[0] <= index - k:
                window.popleft()
            if index >= k - 1:
                result.append(nums[window[0]])
        return result
