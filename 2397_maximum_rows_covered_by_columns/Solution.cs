// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

public class Solution {
    public int MaximumRows(int[][] matrix, int numSelect) {
        int m = matrix.Length, n = matrix[0].Length;
        int ans = 0;
        void Dfs(int col, int chosen, int mask) {
            if (chosen == numSelect) {
                int covered = 0;
                for (int i = 0; i < m; i++) {
                    bool ok = true;
                    for (int j = 0; j < n; j++) {
                        if (matrix[i][j] == 1 && ((mask >> j) & 1) == 0) { ok = false; break; }
                    }
                    if (ok) covered++;
                }
                if (covered > ans) ans = covered;
                return;
            }
            if (col == n) return;
            Dfs(col + 1, chosen + 1, mask | (1 << col));
            Dfs(col + 1, chosen, mask);
        }
        Dfs(0, 0, 0);
        return ans;
    }
}
