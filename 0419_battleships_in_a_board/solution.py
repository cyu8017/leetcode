# LeetCode 0419 - Battleships in a Board
# https://leetcode.com/problems/battleships-in-a-board/

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != "X":
                    continue
                if row > 0 and board[row - 1][col] == "X":
                    continue
                if col > 0 and board[row][col - 1] == "X":
                    continue
                count += 1
        return count
