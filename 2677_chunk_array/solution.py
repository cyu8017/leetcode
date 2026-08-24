# LeetCode 2677 - Chunk Array
# https://leetcode.com/problems/chunk-array/

from typing import Any, List


class Solution:
    def chunk(self, arr: List[Any], size: int) -> List[List[Any]]:
        ans = []
        for i in range(0, len(arr), size):
            ans.append(arr[i:i + size])
        return ans
