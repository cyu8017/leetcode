// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

public class Solution {
    public IList<IList<string>> SolveNQueens(int n) {
        var result = new List<IList<string>>();
        var cols = new HashSet<int>();
        var diag1 = new HashSet<int>();
        var diag2 = new HashSet<int>();
        var board = new string[n];
        for (int i = 0; i < n; i++) {
            board[i] = new string('.', n);
        }

        Backtrack(0, n, board, cols, diag1, diag2, result);
        return result;
    }

    private void Backtrack(
        int row,
        int n,
        string[] board,
        HashSet<int> cols,
        HashSet<int> diag1,
        HashSet<int> diag2,
        IList<IList<string>> result
    ) {
        if (row == n) {
            result.Add(board.ToArray());
            return;
        }

        for (int col = 0; col < n; col++) {
            if (cols.Contains(col) || diag1.Contains(row + col) || diag2.Contains(row - col)) {
                continue;
            }

            cols.Add(col);
            diag1.Add(row + col);
            diag2.Add(row - col);

            var chars = board[row].ToCharArray();
            chars[col] = 'Q';
            board[row] = new string(chars);

            Backtrack(row + 1, n, board, cols, diag1, diag2, result);

            cols.Remove(col);
            diag1.Remove(row + col);
            diag2.Remove(row - col);
            board[row] = new string('.', n);
        }
    }
}
