# LeetCode 0275 - H-Index II
# https://leetcode.com/problems/h-index-ii/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations) - 1
        length = len(citations)
        while left <= right:
            mid = (left + right) // 2
            papers = length - mid
            if citations[mid] >= papers:
                right = mid - 1
            else:
                left = mid + 1
        return length - left
