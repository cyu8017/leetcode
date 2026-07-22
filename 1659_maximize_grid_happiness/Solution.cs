// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

using System;
using System.Collections.Generic;

public class Solution {
    public int GetMaxGridHappiness(int m, int n, int introvertsCount, int extrovertsCount) {
        int states = 1;
        for (int t = 0; t < n; t++) states *= 3;
        int[][] cells = new int[states][];
        int[] intro = new int[states];
        int[] extro = new int[states];
        int[] row = new int[states];
        int[,] compat = new int[states, states];

        for (int s = 0; s < states; s++) {
            int x = s;
            cells[s] = new int[n];
            int val = 0;
            for (int j = 0; j < n; j++) {
                cells[s][j] = x % 3;
                x /= 3;
                int z = cells[s][j];
                if (z == 1) { intro[s]++; val += 120; }
                else if (z == 2) { extro[s]++; val += 40; }
            }
            for (int j = 1; j < n; j++) val += Pair(cells[s][j - 1], cells[s][j]);
            row[s] = val;
        }
        for (int a = 0; a < states; a++) {
            for (int b = 0; b < states; b++) {
                int v = 0;
                for (int j = 0; j < n; j++) v += Pair(cells[a][j], cells[b][j]);
                compat[a, b] = v;
            }
        }

        var memo = new Dictionary<(int, int, int, int), int>();
        int Dfs(int r, int prev, int i, int e) {
            if (r == m) return 0;
            var key = (r, prev, i, e);
            if (memo.TryGetValue(key, out int cached)) return cached;
            int best = 0;
            for (int s = 0; s < states; s++) {
                if (intro[s] > i || extro[s] > e) continue;
                best = Math.Max(best, row[s] + compat[prev, s] + Dfs(r + 1, s, i - intro[s], e - extro[s]));
            }
            return memo[key] = best;
        }
        return Dfs(0, 0, introvertsCount, extrovertsCount);
    }

    private static int Pair(int a, int b) {
        if (a == 0 || b == 0) return 0;
        return (a == 1 ? -30 : 20) + (b == 1 ? -30 : 20);
    }
}
