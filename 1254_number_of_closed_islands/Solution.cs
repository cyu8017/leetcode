// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

using System.Collections.Generic;

public class Solution {
    public int ClosedIsland(int[][] grid) {
        int m = grid.Length, n = grid[0].Length, answer = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0 && Flood(grid, r, c)) answer++;
            }
        }
        return answer;
    }

    private static bool Flood(int[][] grid, int sr, int sc) {
        int m = grid.Length, n = grid[0].Length;
        var stack = new Stack<(int, int)>();
        stack.Push((sr, sc));
        grid[sr][sc] = 1;
        bool closed = true;
        while (stack.Count > 0) {
            var (r, c) = stack.Pop();
            if (r == 0 || r == m - 1 || c == 0 || c == n - 1) closed = false;
            int[] dr = { 1, -1, 0, 0 }, dc = { 0, 0, 1, -1 };
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    stack.Push((nr, nc));
                }
            }
        }
        return closed;
    }
}
