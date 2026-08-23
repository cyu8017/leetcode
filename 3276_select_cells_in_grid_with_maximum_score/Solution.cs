// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxScore(int[][] grid) {
        int m = grid.Length;
        var vals = new Dictionary<int, List<int>>();
        for (int i = 0; i < m; i++) {
            var seen = new HashSet<int>();
            foreach (int v in grid[i]) {
                if (!seen.Contains(v)) {
                    if (!vals.ContainsKey(v)) vals[v] = new List<int>();
                    vals[v].Add(i);
                    seen.Add(v);
                }
            }
        }
        var arr = new List<int>(vals.Keys);
        arr.Sort((a, b) => b.CompareTo(a));
        int N = 1 << m;
        int[] dp = new int[N];
        foreach (int v in arr) {
            int[] ndp = (int[])dp.Clone();
            foreach (int r in vals[v]) {
                int bit = 1 << r;
                for (int mask = 0; mask < N; mask++) {
                    if ((mask & bit) != 0) continue;
                    int cand = dp[mask] + v;
                    int nmask = mask | bit;
                    if (cand > ndp[nmask]) ndp[nmask] = cand;
                }
            }
            dp = ndp;
        }
        int ans = 0;
        foreach (int x in dp) ans = Math.Max(ans, x);
        return ans;
    }
}
