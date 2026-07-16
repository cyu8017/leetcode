# LeetCode 0999 - Available Captures for Rook
# https://leetcode.com/problems/available-captures-for-rook/

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        m, n = len(board), len(board[0])
        r = c = -1
        for i in range(m):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    r, c = i, j
        if r < 0:
            return 0
        ans = 0
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            i, j = r + dr, c + dc
            while 0 <= i < m and 0 <= j < len(board[i]):
                if board[i][j] == "B":
                    break
                if board[i][j] == "p":
                    ans += 1
                    break
                i += dr
                j += dc
        return ans
