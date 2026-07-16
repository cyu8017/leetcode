# LeetCode 0909 - Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/

from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def label(r: int, c: int) -> int:
            row = n - 1 - r
            if row % 2 == 0:
                return row * n + c + 1
            return row * n + (n - c)

        def pos(square: int) -> tuple[int, int]:
            square -= 1
            row = square // n
            rem = square % n
            r = n - 1 - row
            c = rem if row % 2 == 0 else n - 1 - rem
            return r, c

        target = n * n
        queue = deque([1])
        seen = {1}
        moves = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return moves
                for nxt in range(cur + 1, min(cur + 6, target) + 1):
                    r, c = pos(nxt)
                    if board[r][c] != -1:
                        nxt = board[r][c]
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append(nxt)
            moves += 1
        return -1
