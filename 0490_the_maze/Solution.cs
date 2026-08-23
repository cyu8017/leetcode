// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

public class Solution {
    public bool HasPath(int[][] maze, int[] start, int[] destination) {
        int rows = maze.Length;
        int cols = maze[0].Length;
        int[][] directions = new int[][] { new[] { -1, 0 }, new[] { 1, 0 }, new[] { 0, -1 }, new[] { 0, 1 } };
        HashSet<string> visited = new();
        Stack<int[]> stack = new();
        stack.Push(new[] { start[0], start[1] });

        while (stack.Count > 0) {
            int[] cell = stack.Pop();
            int row = cell[0];
            int col = cell[1];
            string key = $"{row},{col}";
            if (visited.Contains(key)) {
                continue;
            }
            visited.Add(key);
            if (row == destination[0] && col == destination[1]) {
                return true;
            }
            foreach (int[] direction in directions) {
                int dr = direction[0];
                int dc = direction[1];
                int nr = row;
                int nc = col;
                while (nr + dr >= 0 && nr + dr < rows && nc + dc >= 0 && nc + dc < cols
                    && maze[nr + dr][nc + dc] == 0) {
                    nr += dr;
                    nc += dc;
                }
                string nextKey = $"{nr},{nc}";
                if (!visited.Contains(nextKey)) {
                    stack.Push(new[] { nr, nc });
                }
            }
        }
        return false;
    }
}
