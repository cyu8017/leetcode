// LeetCode 0052 - N-Queens II
// https://leetcode.com/problems/n-queens-ii/

public class Solution {
    private int count;

    public int TotalNQueens(int n) {
        count = 0;
        var cols = new HashSet<int>();
        var diag1 = new HashSet<int>();
        var diag2 = new HashSet<int>();
        Backtrack(0, n, cols, diag1, diag2);
        return count;
    }

    private void Backtrack(int row, int n, HashSet<int> cols, HashSet<int> diag1, HashSet<int> diag2) {
        if (row == n) {
            count++;
            return;
        }

        for (int col = 0; col < n; col++) {
            if (cols.Contains(col) || diag1.Contains(row + col) || diag2.Contains(row - col)) {
                continue;
            }

            cols.Add(col);
            diag1.Add(row + col);
            diag2.Add(row - col);
            Backtrack(row + 1, n, cols, diag1, diag2);
            cols.Remove(col);
            diag1.Remove(row + col);
            diag2.Remove(row - col);
        }
    }
}
