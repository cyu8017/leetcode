// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

import java.util.*;

class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length, n = maze[0].length;
        int er = entrance[0], ec = entrance[1];
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{er, ec, 0});
        maze[er][ec] = '+';
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int r = cur[0], c = cur[1], d = cur[2];
            for (int[] dir : dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nc >= 0 && nr < m && nc < n && maze[nr][nc] == '.') {
                    if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) return d + 1;
                    maze[nr][nc] = '+';
                    q.offer(new int[]{nr, nc, d + 1});
                }
            }
        }
        return -1;
    }
}
