// LeetCode 0130 - Surrounded Regions
// https://leetcode.com/problems/surrounded-regions/

class Solution {
    public void solve(char[][] board) {
        if (board.length == 0 || board[0].length == 0) return;
        int rows = board.length, cols = board[0].length;
        for (int r = 0; r < rows; r++) {
            mark(board, r, 0);
            mark(board, r, cols - 1);
        }
        for (int c = 0; c < cols; c++) {
            mark(board, 0, c);
            mark(board, rows - 1, c);
        }
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                else if (board[r][c] == 'E') board[r][c] = 'O';
            }
        }
    }

    private void mark(char[][] board, int r, int c) {
        if (r < 0 || r == board.length || c < 0 || c == board[0].length || board[r][c] != 'O') return;
        board[r][c] = 'E';
        mark(board, r + 1, c);
        mark(board, r - 1, c);
        mark(board, r, c + 1);
        mark(board, r, c - 1);
    }
}