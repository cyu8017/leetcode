// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

using System;

public class Solution {
    public int MinSessions(int[] tasks, int sessionTime) {
        int n = tasks.Length;
        var dp = new (int sessions, int used)[1 << n];
        for (int i = 0; i < dp.Length; i++) dp[i] = (n + 1, 0);
        dp[0] = (1, 0);
        for (int mask = 0; mask < (1 << n); mask++) {
            var (sessions, used) = dp[mask];
            if (sessions > n) continue;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                int t = tasks[i], nmask = mask | (1 << i);
                var cand = used + t <= sessionTime ? (sessions, used + t) : (sessions + 1, t);
                if (cand.CompareTo(dp[nmask]) < 0) dp[nmask] = cand;
            }
        }
        return dp[(1 << n) - 1].sessions;
    }
}