# LeetCode 3078 - Match Alphanumerical Pattern in Matrix I
# https://leetcode.com/problems/match-alphanumerical-pattern-in-matrix-i/

from typing import List


class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        m = len(board)
        n = len(board[0])
        r = len(pattern)
        c = len(pattern[0])

        def check(i: int, j: int) -> bool:
            d1 = [0] * 26
            d2 = [0] * 10
            for a in range(r):
                for b in range(c):
                    x = i + a
                    y = j + b
                    ch = pattern[a][b]
                    if "0" <= ch <= "9":
                        if ord(ch) - 48 != board[x][y]:
                            return False
                    else:
                        v = ord(ch) - 97
                        if d1[v] > 0 and d1[v] - 1 != board[x][y]:
                            return False
                        if d2[board[x][y]] > 0 and d2[board[x][y]] - 1 != v:
                            return False
                        d1[v] = board[x][y] + 1
                        d2[board[x][y]] = v + 1
            return True

        for i in range(m - r + 1):
            for j in range(n - c + 1):
                if check(i, j):
                    return [i, j]
        return [-1, -1]
