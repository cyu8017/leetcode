// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

using System.Collections.Generic;

public class Solution {
    public int MinPushBox(char[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[] box = null, player = null, target = null;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 'B') box = new[] { r, c };
                else if (grid[r][c] == 'S') player = new[] { r, c };
                else if (grid[r][c] == 'T') target = new[] { r, c };
            }
        }

        HashSet<int> Reachable(int[] start, int[] blocked) {
            var seen = new HashSet<int> { start[0] * n + start[1] };
            var stack = new Stack<int[]>();
            stack.Push(start);
            while (stack.Count > 0) {
                var cur = stack.Pop();
                foreach (var d in new[] { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } }) {
                    int nr = cur[0] + d[0], nc = cur[1] + d[1];
                    int key = nr * n + nc;
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') continue;
                    if (blocked != null && nr == blocked[0] && nc == blocked[1]) continue;
                    if (seen.Add(key)) stack.Push(new[] { nr, nc });
                }
            }
            return seen;
        }

        var queue = new Queue<(int[] box, int[] player, int pushes)>();
        var seenStates = new HashSet<long>();
        long StateKey(int[] b, int[] p) => ((long)b[0] * n + b[1]) << 20 | (p[0] * n + p[1]);
        queue.Enqueue((box, player, 0));
        seenStates.Add(StateKey(box, player));
        int[][] dirs = { new[] { 1, 0 }, new[] { -1, 0 }, new[] { 0, 1 }, new[] { 0, -1 } };

        while (queue.Count > 0) {
            var (b, p, pushes) = queue.Dequeue();
            if (b[0] == target[0] && b[1] == target[1]) return pushes;
            var canReach = Reachable(p, b);
            foreach (var d in dirs) {
                int[] stand = { b[0] - d[0], b[1] - d[1] };
                int[] nb = { b[0] + d[0], b[1] + d[1] };
                if (!canReach.Contains(stand[0] * n + stand[1])) continue;
                if (nb[0] < 0 || nb[0] >= m || nb[1] < 0 || nb[1] >= n || grid[nb[0]][nb[1]] == '#') continue;
                long key = StateKey(nb, b);
                if (seenStates.Add(key)) queue.Enqueue((nb, b, pushes + 1));
            }
        }
        return -1;
    }
}
