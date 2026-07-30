// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

using System.Collections.Generic;

public class Solution {
    public int NearestExit(char[][] maze, int[] entrance) {
        int m = maze.Length, n = maze[0].Length;
        int er = entrance[0], ec = entrance[1];
        var q = new Queue<(int r, int c, int d)>();
        q.Enqueue((er, ec, 0));
        maze[er][ec] = '+';
        int[] dr = { 1, -1, 0, 0 }, dc = { 0, 0, 1, -1 };
        while (q.Count > 0) {
            var (r, c, d) = q.Dequeue();
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] == '.') {
                    if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) return d + 1;
                    maze[nr][nc] = '+';
                    q.Enqueue((nr, nc, d + 1));
                }
            }
        }
        return -1;
    }
}