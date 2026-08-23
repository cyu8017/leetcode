// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

using System;
using System.Collections.Generic;

public class Solution {
    public int OrderOfLargestPlusSign(int n, int[][] mines) {
        var banned = new HashSet<int>();
        foreach (var mine in mines) banned.Add(mine[0] * n + mine[1]);
        int[][] arms = new int[n][];
        for (int i = 0; i < n; i++) arms[i] = new int[n];
        int best = 0;
        for (int r = 0; r < n; r++) {
            int count = 0;
            for (int c = 0; c < n; c++) {
                count = banned.Contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = count;
            }
            count = 0;
            for (int c = n - 1; c >= 0; c--) {
                count = banned.Contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = Math.Min(arms[r][c], count);
            }
        }
        for (int c = 0; c < n; c++) {
            int count = 0;
            for (int r = 0; r < n; r++) {
                count = banned.Contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = Math.Min(arms[r][c], count);
            }
            count = 0;
            for (int r = n - 1; r >= 0; r--) {
                count = banned.Contains(r * n + c) ? 0 : count + 1;
                arms[r][c] = Math.Min(arms[r][c], count);
                best = Math.Max(best, arms[r][c]);
            }
        }
        return best;
    }
}
