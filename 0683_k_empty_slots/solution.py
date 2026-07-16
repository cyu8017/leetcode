# LeetCode 0683 - K Empty Slots
# https://leetcode.com/problems/k-empty-slots/

from typing import List


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        days = [0] * n
        for day, bulb in enumerate(bulbs, 1):
            days[bulb - 1] = day

        ans = float("inf")
        i = 0
        while i < n - k - 1:
            left, right = i, i + k + 1
            j = left + 1
            while j < right and days[j] > days[left] and days[j] > days[right]:
                j += 1
            if j == right:
                ans = min(ans, max(days[left], days[right]))
                i += 1
            else:
                i = j
        return -1 if ans == float("inf") else int(ans)
