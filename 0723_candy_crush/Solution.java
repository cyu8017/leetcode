// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

class Solution {
    public int[][] candyCrush(int[][] board) {
        int m = board.length, n = board[0].length;
        boolean stable = false;
        while (!stable) {
            stable = true;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n - 2; j++) {
                    int value = Math.abs(board[i][j]);
                    if (value != 0 && value == Math.abs(board[i][j + 1]) && value == Math.abs(board[i][j + 2])) {
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -value;
                        stable = false;
                    }
                }
            }
            for (int j = 0; j < n; j++) {
                for (int i = 0; i < m - 2; i++) {
                    int value = Math.abs(board[i][j]);
                    if (value != 0 && value == Math.abs(board[i + 1][j]) && value == Math.abs(board[i + 2][j])) {
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -value;
                        stable = false;
                    }
                }
            }
            for (int j = 0; j < n; j++) {
                int write = m - 1;
                for (int i = m - 1; i >= 0; i--) {
                    if (board[i][j] > 0) board[write--][j] = board[i][j];
                }
                for (int i = write; i >= 0; i--) board[i][j] = 0;
            }
        }
        return board;
    }
}
