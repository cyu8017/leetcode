// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

using System;

public class Solution {
    public long[] MinimumCosts(int[] regular, int[] express, int expressCost) {
        int n = regular.Length;
        long[] ans = new long[n];
        long reg = 0, exp = expressCost;
        for (int i = 0; i < n; i++) {
            long nextReg = Math.Min(reg + regular[i], exp + express[i]);
            long nextExp = Math.Min(reg + regular[i] + expressCost, exp + express[i]);
            reg = nextReg;
            exp = nextExp;
            ans[i] = Math.Min(reg, exp);
        }
        return ans;
    }
}
