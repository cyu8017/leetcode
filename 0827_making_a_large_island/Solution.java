// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

import java.util.*;

class Solution {
    private int[][] grid;
    private int n;

    public int largestIsland(int[][] grid) {
        this.grid = grid;
        n = grid.length;
        Map<Integer, Integer> sizes = new HashMap<>();
        sizes.put(0, 0);
        int islandId = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    sizes.put(islandId, dfs(i, j, islandId));
                    islandId++;
                }
            }
        }
        int ans = 0;
        for (int v : sizes.values()) ans = Math.max(ans, v);
        int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0) continue;
                Set<Integer> seen = new HashSet<>();
                int total = 1;
                for (int k = 0; k < 4; k++) {
                    int ni = i + dr[k], nj = j + dc[k];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        int iid = grid[ni][nj];
                        if (iid > 1 && seen.add(iid)) total += sizes.get(iid);
                    }
                }
                ans = Math.max(ans, total);
            }
        }
        return ans;
    }

    private int dfs(int r, int c, int iid) {
        if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return 0;
        grid[r][c] = iid;
        return 1 + dfs(r + 1, c, iid) + dfs(r - 1, c, iid) + dfs(r, c + 1, iid) + dfs(r, c - 1, iid);
    }
}
