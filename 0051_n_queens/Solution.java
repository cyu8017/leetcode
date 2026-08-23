// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        Set<Integer> cols = new HashSet<>();
        Set<Integer> diag1 = new HashSet<>();
        Set<Integer> diag2 = new HashSet<>();
        char[][] board = new char[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }

        backtrack(0, n, board, cols, diag1, diag2, result);
        return result;
    }

    private void backtrack(
        int row,
        int n,
        char[][] board,
        Set<Integer> cols,
        Set<Integer> diag1,
        Set<Integer> diag2,
        List<List<String>> result
    ) {
        if (row == n) {
            List<String> snapshot = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                snapshot.add(new String(board[i]));
            }
            result.add(snapshot);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (cols.contains(col) || diag1.contains(row + col) || diag2.contains(row - col)) {
                continue;
            }

            cols.add(col);
            diag1.add(row + col);
            diag2.add(row - col);
            board[row][col] = 'Q';

            backtrack(row + 1, n, board, cols, diag1, diag2, result);

            cols.remove(col);
            diag1.remove(row + col);
            diag2.remove(row - col);
            board[row][col] = '.';
        }
    }
}
