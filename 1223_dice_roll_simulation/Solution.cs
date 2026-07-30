// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

using System.Collections.Generic;

public class Solution {
    public int DieSimulator(int n, int[] rollMax) {
        const int mod = 1_000_000_007;
        var dp = new List<int[]>();
        for (int j = 0; j < 6; j++) {
            var row = new int[rollMax[j] + 1];
            row[1] = 1;
            dp.Add(row);
        }
        for (int roll = 1; roll < n; roll++) {
            var totals = new int[6];
            for (int j = 0; j < 6; j++) {
                int sum = 0;
                for (int k = 1; k < dp[j].Length; k++) sum = (sum + dp[j][k]) % mod;
                totals[j] = sum;
            }
            var nxt = new List<int[]>();
            for (int j = 0; j < 6; j++) {
                var row = new int[rollMax[j] + 1];
                int allExcept = 0;
                for (int t = 0; t < 6; t++) {
                    if (t != j) allExcept = (allExcept + totals[t]) % mod;
                }
                row[1] = allExcept;
                for (int run = 2; run < row.Length; run++) {
                    row[run] = dp[j][run - 1];
                }
                nxt.Add(row);
            }
            dp = nxt;
        }
        int ans = 0;
        foreach (var row in dp) {
            for (int k = 1; k < row.Length; k++) ans = (ans + row[k]) % mod;
        }
        return ans;
    }
}
