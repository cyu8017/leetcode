// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution {
    private int[][] matrix;
    private int m, n, numSelect, ans;

    public int maximumRows(int[][] matrix, int numSelect) {
        this.matrix = matrix;
        this.numSelect = numSelect;
        m = matrix.length;
        n = matrix[0].length;
        ans = 0;
        dfs(0, 0, 0);
        return ans;
    }

    private void dfs(int col, int chosen, int mask) {
        if (chosen == numSelect) {
            int covered = 0;
            for (int i = 0; i < m; i++) {
                boolean ok = true;
                for (int j = 0; j < n; j++) {
                    if (matrix[i][j] == 1 && ((mask >> j) & 1) == 0) {
                        ok = false;
                        break;
                    }
                }
                if (ok) covered++;
            }
            ans = Math.max(ans, covered);
            return;
        }
        if (col == n) return;
        dfs(col + 1, chosen + 1, mask | (1 << col));
        dfs(col + 1, chosen, mask);
    }
}
