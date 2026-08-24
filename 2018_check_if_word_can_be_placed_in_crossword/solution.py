# LeetCode 2018 - Check if Word Can Be Placed In Crossword
# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        m, n, L = len(board), len(board[0]), len(word)

        def match(cells: str) -> bool:
            if len(cells) != L:
                return False
            ok1 = ok2 = True
            for i in range(L):
                if cells[i] != " " and cells[i] != word[i]:
                    ok1 = False
                if cells[i] != " " and cells[i] != word[L - 1 - i]:
                    ok2 = False
            return ok1 or ok2

        for r in range(m):
            c = 0
            while c < n:
                while c < n and board[r][c] == "#":
                    c += 1
                start = c
                while c < n and board[r][c] != "#":
                    c += 1
                if c - start == L:
                    sb = "".join(board[r][i] for i in range(start, c))
                    if match(sb):
                        return True
        for c in range(n):
            r = 0
            while r < m:
                while r < m and board[r][c] == "#":
                    r += 1
                start = r
                while r < m and board[r][c] != "#":
                    r += 1
                if r - start == L:
                    sb = "".join(board[start + i][c] for i in range(L))
                    if match(sb):
                        return True
        return False
