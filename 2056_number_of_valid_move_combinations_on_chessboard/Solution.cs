// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

using System;
using System.Collections.Generic;

public class Solution {
    private struct Move { public int dr, dc, steps; public Move(int dr, int dc, int steps) { this.dr = dr; this.dc = dc; this.steps = steps; } }

    public int CountCombinations(string[] pieces, int[][] positions) {
        var dirs = new Dictionary<string, (int, int)[]> {
            ["rook"] = new[] { (1,0), (-1,0), (0,1), (0,-1) },
            ["bishop"] = new[] { (1,1), (1,-1), (-1,1), (-1,-1) },
            ["queen"] = new[] { (1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1) },
        };
        int n = pieces.Length;
        var allMoves = new List<Move>[n];
        for (int i = 0; i < n; i++) {
            var ms = new List<Move> { new Move(0, 0, 0) };
            int r = positions[i][0], c = positions[i][1];
            foreach (var (dr, dc) in dirs[pieces[i]]) {
                int nr = r + dr, nc = c + dc, step = 1;
                while (nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8) {
                    ms.Add(new Move(dr, dc, step));
                    nr += dr; nc += dc; step++;
                }
            }
            allMoves[i] = ms;
        }
        var chosen = new Move[n];
        bool OkCombo(int end) {
            int maxT = 0;
            for (int i = 0; i <= end; i++) maxT = Math.Max(maxT, chosen[i].steps);
            for (int t = 1; t <= maxT; t++) {
                var pos = new Dictionary<(int, int), int>();
                for (int i = 0; i <= end; i++) {
                    var m = chosen[i];
                    int pr, pc;
                    if (m.steps == 0) { pr = positions[i][0]; pc = positions[i][1]; }
                    else {
                        int use = Math.Min(t, m.steps);
                        pr = positions[i][0] + m.dr * use;
                        pc = positions[i][1] + m.dc * use;
                    }
                    if (pos.ContainsKey((pr, pc))) return false;
                    pos[(pr, pc)] = i;
                }
            }
            return true;
        }
        int ans = 0;
        void Dfs(int i) {
            if (i == n) { ans++; return; }
            foreach (var m in allMoves[i]) {
                chosen[i] = m;
                if (OkCombo(i)) Dfs(i + 1);
            }
        }
        Dfs(0);
        return ans;
    }
}
