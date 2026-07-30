// LeetCode 1368 - Minimum Cost To Make At Least One Valid Path In A Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

using System.Collections.Generic;
public class Solution {
    public int MinCost(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        var dist = new int[m, n];
        for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) dist[i, j] = int.MaxValue / 4;
        dist[0, 0] = 0;
        var q = new LinkedList<(int, int)>();
        q.AddFirst((0, 0));
        int[][] dirs = { new[]{0,1}, new[]{0,-1}, new[]{1,0}, new[]{-1,0} };
        while (q.Count > 0) {
            var (r, c) = q.First.Value; q.RemoveFirst();
            for (int k = 0; k < 4; k++) {
                int x = r + dirs[k][0], y = c + dirs[k][1];
                if (x >= 0 && x < m && y >= 0 && y < n) {
                    int w = k + 1 != grid[r][c] ? 1 : 0;
                    int nd = dist[r, c] + w;
                    if (nd < dist[x, y]) {
                        dist[x, y] = nd;
                        if (w == 0) q.AddFirst((x, y)); else q.AddLast((x, y));
                    }
                }
            }
        }
        return dist[m - 1, n - 1];
    }
}
