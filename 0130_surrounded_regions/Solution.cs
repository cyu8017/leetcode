// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

public class Solution {
    public void Solve(char[][] board) {
        if (board.Length == 0 || board[0].Length == 0) return;
        int rows = board.Length, cols = board[0].Length;
        for (int r = 0; r < rows; r++) {
            Mark(board, r, 0);
            Mark(board, r, cols - 1);
        }
        for (int c = 0; c < cols; c++) {
            Mark(board, 0, c);
            Mark(board, rows - 1, c);
        }
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                else if (board[r][c] == 'E') board[r][c] = 'O';
            }
        }
    }

    private void Mark(char[][] board, int r, int c) {
        if (r < 0 || r == board.Length || c < 0 || c == board[0].Length || board[r][c] != 'O') return;
        board[r][c] = 'E';
        Mark(board, r + 1, c);
        Mark(board, r - 1, c);
        Mark(board, r, c + 1);
        Mark(board, r, c - 1);
    }
}