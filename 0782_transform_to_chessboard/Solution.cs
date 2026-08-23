// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

using System;

public class Solution {
    public int MovesToChessboard(int[][] board) {
        int n = board.Length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0) return -1;
            }
        }
        int rowSum = 0, colSum = 0;
        for (int i = 0; i < n; i++) {
            rowSum += board[0][i];
            colSum += board[i][0];
        }
        if (!(n / 2 <= rowSum && rowSum <= (n + 1) / 2)) return -1;
        if (!(n / 2 <= colSum && colSum <= (n + 1) / 2)) return -1;
        int rowSwap = 0, colSwap = 0;
        for (int i = 0; i < n; i++) {
            rowSwap += board[0][i] != i % 2 ? 1 : 0;
            colSwap += board[i][0] != i % 2 ? 1 : 0;
        }
        if (n % 2 != 0) {
            if (rowSwap % 2 != 0) rowSwap = n - rowSwap;
            if (colSwap % 2 != 0) colSwap = n - colSwap;
        } else {
            rowSwap = Math.Min(rowSwap, n - rowSwap);
            colSwap = Math.Min(colSwap, n - colSwap);
        }
        return (rowSwap + colSwap) / 2;
    }
}
