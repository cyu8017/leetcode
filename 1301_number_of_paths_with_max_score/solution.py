# LeetCode 1301 - Number Of Paths With Max Score

from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 1_000_000_007
        n = len(board)
        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]
        score[n - 1][n - 1], ways[n - 1][n - 1] = 0, 1
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == "X" or (r == n - 1 and c == n - 1):
                    continue
                best = -1
                count = 0
                for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
                    if nr < n and nc < n and score[nr][nc] >= 0:
                        if score[nr][nc] > best:
                            best, count = score[nr][nc], ways[nr][nc]
                        elif score[nr][nc] == best:
                            count = (count + ways[nr][nc]) % mod
                if best >= 0:
                    score[r][c] = best + (int(board[r][c]) if board[r][c].isdigit() else 0)
                    ways[r][c] = count
        return [max(score[0][0], 0), ways[0][0]]
