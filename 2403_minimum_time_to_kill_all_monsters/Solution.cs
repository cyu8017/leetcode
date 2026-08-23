// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

using System;

public class Solution {
    public long MinimumTime(int[] power) {
        int n = power.Length;
        int N = 1 << n;
        long[] dp = new long[N];
        Array.Fill(dp, long.MaxValue / 4);
        dp[0] = 0;
        for (int mask = 0; mask < N; mask++) {
            int killed = BitCount(mask);
            long gain = killed + 1;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                long need = (power[i] + gain - 1) / gain;
                int nm = mask | (1 << i);
                dp[nm] = Math.Min(dp[nm], dp[mask] + need);
            }
        }
        return dp[N - 1];
    }

    private static int BitCount(int x) {
        int c = 0;
        while (x != 0) { c += x & 1; x >>= 1; }
        return c;
    }
}
