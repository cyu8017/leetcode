// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

import java.util.*;

class Solution {
    private List<Integer>[] g;
    private int[] match;

    private boolean dfs(int u, boolean[] seen) {
        for (int v : g[u]) {
            if (seen[v]) continue;
            seen[v] = true;
            if (match[v] == -1 || dfs(match[v], seen)) {
                match[v] = u;
                return true;
            }
        }
        return false;
    }

    public int minimumOperations(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] id = new int[m][n];
        for (int i = 0; i < m; i++) Arrays.fill(id[i], -1);
        int cnt = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) id[i][j] = cnt++;
        g = new ArrayList[cnt];
        for (int i = 0; i < cnt; i++) g[i] = new ArrayList<>();
        int[][] dirs = {{0,1},{1,0},{0,-1},{-1,0}};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 1 || (i + j) % 2 != 0) continue;
                int u = id[i][j];
                for (int[] d : dirs) {
                    int ni = i + d[0], nj = j + d[1];
                    if (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1)
                        g[u].add(id[ni][nj]);
                }
            }
        }
        match = new int[cnt];
        Arrays.fill(match, -1);
        int ans = 0;
        for (int u = 0; u < cnt; u++) {
            boolean ok = false;
            for (int i = 0; i < m && !ok; i++)
                for (int j = 0; j < n; j++)
                    if (id[i][j] == u && (i + j) % 2 == 0) { ok = true; break; }
            if (!ok) continue;
            boolean[] seen = new boolean[cnt];
            if (dfs(u, seen)) ans++;
        }
        return ans;
    }
}
