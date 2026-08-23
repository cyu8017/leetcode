// LeetCode 3359 - Find Sorted Submatrices With Maximum Element at Most K
// https://leetcode.com/problems/find-sorted-submatrices-with-maximum-element-at-most-k/

class Solution {
    public long countSortedMatrices(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        long ans = 0;
        for (int r1 = 0; r1 < m; r1++) {
            for (int r2 = r1; r2 < m; r2++) {
                for (int c1 = 0; c1 < n; c1++) {
                    for (int c2 = c1; c2 < n; c2++) {
                        boolean ok = true;
                        for (int i = r1; i <= r2 && ok; i++) {
                            for (int j = c1; j <= c2; j++) {
                                if (grid[i][j] > k) { ok = false; break; }
                                if (j > c1 && grid[i][j] < grid[i][j - 1]) { ok = false; break; }
                                if (i > r1 && grid[i][j] < grid[i - 1][j]) { ok = false; break; }
                            }
                        }
                        if (ok) ans++;
                    }
                }
            }
        }
        return ans;
    }
}
