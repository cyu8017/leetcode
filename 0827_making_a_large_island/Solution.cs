// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

using System;
using System.Collections.Generic;

public class Solution {
    public int LargestIsland(int[][] grid) {
        int n = grid.Length;
        var sizes = new Dictionary<int, int> { [0] = 0 };
        int islandId = 2;
        int Dfs(int r, int c, int iid) {
            if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1) return 0;
            grid[r][c] = iid;
            return 1 + Dfs(r + 1, c, iid) + Dfs(r - 1, c, iid) + Dfs(r, c + 1, iid) + Dfs(r, c - 1, iid);
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (grid[i][j] == 1) { sizes[islandId] = Dfs(i, j, islandId); islandId++; }
        int ans = 0;
        foreach (var v in sizes.Values) ans = Math.Max(ans, v);
        int[] dr = { 1, -1, 0, 0 }, dc = { 0, 0, 1, -1 };
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != 0) continue;
                var seen = new HashSet<int>();
                int total = 1;
                for (int k = 0; k < 4; k++) {
                    int ni = i + dr[k], nj = j + dc[k];
                    if (ni >= 0 && ni < n && nj >= 0 && nj < n) {
                        int iid = grid[ni][nj];
                        if (iid > 1 && seen.Add(iid)) total += sizes[iid];
                    }
                }
                ans = Math.Max(ans, total);
            }
        }
        return ans;
    }
}
