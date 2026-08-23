// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindPath(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        ulong st = 0;
        var path = new List<IList<int>>();
        int[] dirs = { -1, 0, 1, 0, -1 };
        int F(int i, int j) => i * n + j;

        bool Dfs(int i, int j, int v) {
            path.Add(new List<int> { i, j });
            if (path.Count == m * n) return true;
            int idx = F(i, j);
            st |= 1UL << idx;
            if (grid[i][j] == v) v++;
            for (int t = 0; t < 4; t++) {
                int x = i + dirs[t], y = j + dirs[t + 1];
                if (0 <= x && x < m && 0 <= y && y < n) {
                    int idx2 = F(x, y);
                    if (((st >> idx2) & 1UL) == 0 && (grid[x][y] == 0 || grid[x][y] == v)) {
                        if (Dfs(x, y, v)) return true;
                    }
                }
            }
            path.RemoveAt(path.Count - 1);
            st ^= 1UL << idx;
            return false;
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 || grid[i][j] == 1) {
                    if (Dfs(i, j, 1)) return path;
                    path.Clear();
                    st = 0;
                }
            }
        }
        return new List<IList<int>>();
    }
}
