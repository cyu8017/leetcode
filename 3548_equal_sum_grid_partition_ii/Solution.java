// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    int[][] rotate(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] t = new int[n][m];
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) t[j][i] = grid[i][j];
        return t;
    }

    boolean check(int[][] g) {
        int m = g.length, n = g[0].length;
        long s1 = 0, s2 = 0;
        Map<Long, Integer> cnt1 = new HashMap<>();
        Map<Long, Integer> cnt2 = new HashMap<>();
        for (int[] row : g) for (int x : row) {
            long v = x;
            s2 += v;
            cnt2.merge(v, 1, Integer::sum);
        }
        for (int i = 0; i < m - 1; i++) {
            for (int x : g[i]) {
                long v = x;
                s1 += v; s2 -= v;
                cnt1.merge(v, 1, Integer::sum);
                cnt2.put(v, cnt2.get(v) - 1);
            }
            if (s1 == s2) return true;
            if (s1 < s2) {
                long diff = s2 - s1;
                if (cnt2.getOrDefault(diff, 0) > 0) {
                    if ((m - i - 1 > 1 && n > 1) ||
                        (i == m - 2 && (g[i + 1][0] == diff || g[i + 1][n - 1] == diff)) ||
                        (n == 1 && (g[i + 1][0] == diff || g[m - 1][0] == diff)))
                        return true;
                }
            } else {
                long diff = s1 - s2;
                if (cnt1.getOrDefault(diff, 0) > 0) {
                    if ((i + 1 > 1 && n > 1) ||
                        (i == 0 && (g[0][0] == diff || g[0][n - 1] == diff)) ||
                        (n == 1 && (g[0][0] == diff || g[i][0] == diff)))
                        return true;
                }
            }
        }
        return false;
    }

    public boolean canPartitionGrid(int[][] grid) {
        return check(grid) || check(rotate(grid));
    }
}
