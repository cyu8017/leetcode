# LeetCode 0279 - Perfect Squares
# https://leetcode.com/problems/perfect-squares/

from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        squares: list[int] = []
        value = 1
        while value * value <= n:
            squares.append(value * value)
            value += 1
        queue = deque([(n, 0)])
        visited = {n}
        while queue:
            remain, steps = queue.popleft()
            if remain == 0:
                return steps
            for square in squares:
                nxt = remain - square
                if nxt < 0:
                    break
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
        return 0
