// LeetCode 1210 - Minimum Moves to Reach Target With Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

using System.Collections.Generic;

public class Solution {
    public int MinimumMoves(int[][] grid) {
        int n = grid.Length;
        var start = (0, 0, 0);
        var target = (n - 1, n - 2, 0);
        var q = new Queue<(int r, int c, int orient, int moves)>();
        var seen = new HashSet<(int, int, int)> { start };
        q.Enqueue((start.Item1, start.Item2, start.Item3, 0));

        while (q.Count > 0) {
            var (r, c, orient, moves) = q.Dequeue();
            if ((r, c, orient) == target) return moves;

            var next = new List<(int, int, int)>();
            if (orient == 0) {
                if (c + 2 < n && grid[r][c + 2] == 0) next.Add((r, c + 1, 0));
                if (r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0) {
                    next.Add((r + 1, c, 0));
                    next.Add((r, c, 1));
                }
            } else {
                if (r + 2 < n && grid[r + 2][c] == 0) next.Add((r + 1, c, 1));
                if (c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0) {
                    next.Add((r, c + 1, 1));
                    next.Add((r, c, 0));
                }
            }

            foreach (var state in next) {
                if (seen.Add(state)) q.Enqueue((state.Item1, state.Item2, state.Item3, moves + 1));
            }
        }
        return -1;
    }
}
