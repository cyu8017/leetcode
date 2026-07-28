// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

using System.Collections.Generic;

public class Solution {
    public int[] GridIllumination(int n, int[][] lamps, int[][] queries) {
        var rows = new Dictionary<int, int>();
        var cols = new Dictionary<int, int>();
        var diag1 = new Dictionary<int, int>();
        var diag2 = new Dictionary<int, int>();
        var lit = new HashSet<(int, int)>();

        void Inc(Dictionary<int, int> d, int key) {
            d.TryGetValue(key, out int v);
            d[key] = v + 1;
        }
        void Dec(Dictionary<int, int> d, int key) {
            d[key]--;
        }
        int Get(Dictionary<int, int> d, int key) => d.TryGetValue(key, out int v) ? v : 0;

        foreach (var lamp in lamps) {
            int r = lamp[0], c = lamp[1];
            if (!lit.Add((r, c))) continue;
            Inc(rows, r); Inc(cols, c); Inc(diag1, r - c); Inc(diag2, r + c);
        }

        var ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int r = queries[qi][0], c = queries[qi][1];
            ans[qi] = (Get(rows, r) > 0 || Get(cols, c) > 0 || Get(diag1, r - c) > 0 || Get(diag2, r + c) > 0) ? 1 : 0;
            for (int i = r - 1; i <= r + 1; i++) {
                for (int j = c - 1; j <= c + 1; j++) {
                    if (lit.Remove((i, j))) {
                        Dec(rows, i); Dec(cols, j); Dec(diag1, i - j); Dec(diag2, i + j);
                    }
                }
            }
        }
        return ans;
    }
}
