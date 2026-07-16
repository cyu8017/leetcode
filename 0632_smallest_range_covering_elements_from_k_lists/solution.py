# LeetCode 0632 - Smallest Range Covering Elements from K Lists
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap: list[tuple[int, int, int]] = []
        current_max = float("-inf")

        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            current_max = max(current_max, arr[0])

        best_left, best_right = heap[0][0], current_max

        while True:
            value, list_index, index = heapq.heappop(heap)
            if current_max - value < best_right - best_left:
                best_left, best_right = value, current_max
            if index + 1 == len(nums[list_index]):
                break
            nxt = nums[list_index][index + 1]
            heapq.heappush(heap, (nxt, list_index, index + 1))
            current_max = max(current_max, nxt)

        return [best_left, best_right]
