// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

using System.Collections.Generic;

public class Solution {
    public int OrangesRotting(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        var q = new Queue<(int r, int c)>();
        int fresh = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) q.Enqueue((i, j));
                else if (grid[i][j] == 1) fresh++;
            }
        }
        int minutes = 0;
        int[][] dirs = new int[][] { new[]{1,0}, new[]{-1,0}, new[]{0,1}, new[]{0,-1} };
        while (q.Count > 0 && fresh > 0) {
            int sz = q.Count;
            for (int s = 0; s < sz; s++) {
                var (r, c) = q.Dequeue();
                foreach (var d in dirs) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        fresh--;
                        q.Enqueue((nr, nc));
                    }
                }
            }
            minutes++;
        }
        return fresh == 0 ? minutes : -1;
    }
}
