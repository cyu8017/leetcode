// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

using System;

public class Solution {
    public long MaximumScore(int[][] grid) {
        int n = grid.Length;
        long[][] prefix = new long[n][];
        for (int j = 0; j < n; j++) {
            prefix[j] = new long[n + 1];
            for (int i = 0; i < n; i++) prefix[j][i + 1] = prefix[j][i] + grid[i][j];
        }
        long[] prevPick = new long[n + 1], prevSkip = new long[n + 1];
        for (int j = 1; j < n; j++) {
            long[] currPick = new long[n + 1], currSkip = new long[n + 1];
            for (int curr = 0; curr <= n; curr++) {
                for (int prev = 0; prev <= n; prev++) {
                    if (curr > prev) {
                        long score = prefix[j - 1][curr] - prefix[j - 1][prev];
                        currPick[curr] = Math.Max(currPick[curr], prevSkip[prev] + score);
                        currSkip[curr] = Math.Max(currSkip[curr], prevSkip[prev] + score);
                    } else {
                        long score = prefix[j][prev] - prefix[j][curr];
                        currPick[curr] = Math.Max(currPick[curr], prevPick[prev] + score);
                        currSkip[curr] = Math.Max(currSkip[curr], prevPick[prev]);
                    }
                }
            }
            prevPick = currPick;
            prevSkip = currSkip;
        }
        long ans = long.MinValue;
        foreach (long v in prevPick) ans = Math.Max(ans, v);
        return ans;
    }
}
