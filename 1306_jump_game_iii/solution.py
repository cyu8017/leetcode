# LeetCode 1306 - Jump Game Iii

from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack, seen = [start], set()
        while stack:
            i = stack.pop()
            if i in seen or not 0 <= i < len(arr):
                continue
            if arr[i] == 0:
                return True
            seen.add(i)
            stack.extend((i - arr[i], i + arr[i]))
        return False
