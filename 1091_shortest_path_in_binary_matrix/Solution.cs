// LeetCode 1091 - Shortest Path in Binary Matrix
// https://leetcode.com/problems/shortest-path-in-binary-matrix/

using System.Collections.Generic;

public class Solution {
    public int ShortestPathBinaryMatrix(int[][] grid) {
        int n = grid.Length;
        if (grid[0][0] != 0 || grid[n - 1][n - 1] != 0) {
            return -1;
        }
        var queue = new Queue<(int r, int c, int dist)>();
        queue.Enqueue((0, 0, 1));
        grid[0][0] = 1;
        while (queue.Count > 0) {
            var (r, c, dist) = queue.Dequeue();
            if (r == n - 1 && c == n - 1) {
                return dist;
            }
            for (int dr = -1; dr <= 1; dr++) {
                for (int dc = -1; dc <= 1; dc++) {
                    if (dr == 0 && dc == 0) {
                        continue;
                    }
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                        grid[nr][nc] = 1;
                        queue.Enqueue((nr, nc, dist + 1));
                    }
                }
            }
        }
        return -1;
    }
}
