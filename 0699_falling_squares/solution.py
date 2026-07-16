# LeetCode 0699 - Falling Squares
# https://leetcode.com/problems/falling-squares/

from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals: list[tuple[int, int, int]] = []
        answer: list[int] = []
        max_height = 0

        for left, side in positions:
            right = left + side
            base = 0
            for l, r, height in intervals:
                if r > left and l < right:
                    base = max(base, height)
            height = base + side
            intervals.append((left, right, height))
            max_height = max(max_height, height)
            answer.append(max_height)

        return answer
