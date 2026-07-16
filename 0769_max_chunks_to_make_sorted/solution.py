# LeetCode 0769 - Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = max_so_far = 0
        for i, value in enumerate(arr):
            max_so_far = max(max_so_far, value)
            if max_so_far == i:
                chunks += 1
        return chunks
