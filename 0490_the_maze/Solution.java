// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int rows = maze.length;
        int cols = maze[0].length;
        int[][] directions = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Set<String> visited = new HashSet<>();
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] {start[0], start[1]});

        while (!stack.isEmpty()) {
            int[] cell = stack.pop();
            int row = cell[0];
            int col = cell[1];
            String key = row + "," + col;
            if (visited.contains(key)) {
                continue;
            }
            visited.add(key);
            if (row == destination[0] && col == destination[1]) {
                return true;
            }
            for (int[] direction : directions) {
                int dr = direction[0];
                int dc = direction[1];
                int nr = row;
                int nc = col;
                while (nr + dr >= 0 && nr + dr < rows && nc + dc >= 0 && nc + dc < cols
                        && maze[nr + dr][nc + dc] == 0) {
                    nr += dr;
                    nc += dc;
                }
                String nextKey = nr + "," + nc;
                if (!visited.contains(nextKey)) {
                    stack.push(new int[] {nr, nc});
                }
            }
        }
        return false;
    }
}
