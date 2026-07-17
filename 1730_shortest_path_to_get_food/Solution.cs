// LeetCode 1730 - Shortest Path to Get Food
// https://leetcode.com/problems/shortest-path-to-get-food/

using System.Collections.Generic;

public class Solution {
    public int GetFood(char[][] grid) {
        int rows = grid.Length;
        int cols = grid[0].Length;
        var queue = new Queue<int[]>();
        bool[,] seen = new bool[rows, cols];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '*') {
                    queue.Enqueue(new[] { r, c, 0 });
                    seen[r, c] = true;
                }
            }
        }
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };
        while (queue.Count > 0) {
            int[] entry = queue.Dequeue();
            int r = entry[0];
            int c = entry[1];
            int d = entry[2];
            if (grid[r][c] == '#') {
                return d;
            }
            foreach (int[] dir in dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr, nc] && grid[nr][nc] != 'X') {
                    seen[nr, nc] = true;
                    queue.Enqueue(new[] { nr, nc, d + 1 });
                }
            }
        }
        return -1;
    }
}
