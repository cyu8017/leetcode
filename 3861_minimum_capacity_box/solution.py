# LeetCode 3861 - Minimum Capacity Box
# https://leetcode.com/problems/minimum-capacity-box/

from typing import List


class Solution:
    def minimumIndex(self, capacity: List[int], itemSize: int) -> int:
        ans = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize and (ans == -1 or capacity[i] < capacity[ans]):
                ans = i
        return ans
