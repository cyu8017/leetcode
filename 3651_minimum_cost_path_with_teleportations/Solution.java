// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class Solution {
    public int minCost(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int inf = Integer.MAX_VALUE / 4;
        int[][][] f = new int[k + 1][m][n];
        for (int t = 0; t <= k; t++)
            for (int i = 0; i < m; i++) Arrays.fill(f[t][i], inf);
        f[0][0][0] = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i > 0) f[0][i][j] = Math.min(f[0][i][j], f[0][i - 1][j] + grid[i][j]);
                if (j > 0) f[0][i][j] = Math.min(f[0][i][j], f[0][i][j - 1] + grid[i][j]);
            }
        }
        TreeMap<Integer, List<int[]>> g = new TreeMap<>((a, b) -> Integer.compare(b, a));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                g.computeIfAbsent(grid[i][j], x -> new ArrayList<>()).add(new int[] {i, j});
        for (int t = 1; t <= k; t++) {
            int mn = inf;
            for (List<int[]> pos : g.values()) {
                for (int[] p : pos) mn = Math.min(mn, f[t - 1][p[0]][p[1]]);
                for (int[] p : pos) f[t][p[0]][p[1]] = mn;
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i > 0) f[t][i][j] = Math.min(f[t][i][j], f[t][i - 1][j] + grid[i][j]);
                    if (j > 0) f[t][i][j] = Math.min(f[t][i][j], f[t][i][j - 1] + grid[i][j]);
                }
            }
        }
        int ans = inf;
        for (int t = 0; t <= k; t++) ans = Math.min(ans, f[t][m - 1][n - 1]);
        return ans;
    }
}
