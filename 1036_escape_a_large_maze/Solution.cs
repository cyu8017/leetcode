// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

using System.Collections.Generic;

public class Solution {
    public bool IsEscapePossible(int[][] blocked, int[] source, int[] target) {
        var blockedSet = new HashSet<(int, int)>();
        foreach (var b in blocked) blockedSet.Add((b[0], b[1]));
        int limit = blocked.Length * (blocked.Length - 1) / 2;
        return Bfs(source, target, blockedSet, limit) && Bfs(target, source, blockedSet, limit);
    }

    private static bool Bfs(int[] start, int[] goal, HashSet<(int, int)> blocked, int limit) {
        var queue = new Queue<(int, int)>();
        var seen = new HashSet<(int, int)>();
        queue.Enqueue((start[0], start[1]));
        seen.Add((start[0], start[1]));
        int[] dr = { 1, -1, 0, 0 }, dc = { 0, 0, 1, -1 };
        while (queue.Count > 0) {
            if (seen.Count > limit) return true;
            var (r, c) = queue.Dequeue();
            if (r == goal[0] && c == goal[1]) return true;
            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d], nc = c + dc[d];
                if (nr >= 0 && nr < 1000000 && nc >= 0 && nc < 1000000
                    && !blocked.Contains((nr, nc)) && seen.Add((nr, nc)))
                    queue.Enqueue((nr, nc));
            }
        }
        return false;
    }
}
