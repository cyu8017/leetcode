// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

using System;
public class Solution {
    public int MinDistance(int[] houses, int k) {
        Array.Sort(houses); int n = houses.Length;
        var cost = new int[n, n];
        for (int i = 0; i < n; i++)
            for (int j = i; j < n; j++) {
                int mid = houses[(i + j) / 2], s = 0;
                for (int t = i; t <= j; t++) s += Math.Abs(houses[t] - mid);
                cost[i, j] = s;
            }
        var dp = new long[n + 1];
        for (int i = 1; i <= n; i++) dp[i] = long.MaxValue / 4;
        for (int box = 0; box < k; box++) {
            var ndp = new long[n + 1];
            for (int i = 1; i <= n; i++) ndp[i] = long.MaxValue / 4;
            for (int j = 1; j <= n; j++)
                for (int i = 0; i < j; i++)
                    ndp[j] = Math.Min(ndp[j], dp[i] + cost[i, j - 1]);
            dp = ndp;
        }
        return (int)dp[n];
    }
}
