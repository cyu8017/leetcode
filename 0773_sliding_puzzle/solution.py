# LeetCode 0773 - Sliding Puzzle
# https://leetcode.com/problems/sliding-puzzle/

from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = "".join(str(cell) for row in board for cell in row)
        target = "123450"
        neighbors = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4),
        }
        queue = deque([(start, 0)])
        seen = {start}
        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            zero = state.index("0")
            for nei in neighbors[zero]:
                chars = list(state)
                chars[zero], chars[nei] = chars[nei], chars[zero]
                nxt = "".join(chars)
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, steps + 1))
        return -1
