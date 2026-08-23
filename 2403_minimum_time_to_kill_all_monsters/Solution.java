// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

import java.util.Arrays;

class Solution {
    public long minimumTime(int[] power) {
        int n = power.length;
        int N = 1 << n;
        long[] dp = new long[N];
        Arrays.fill(dp, Long.MAX_VALUE / 4);
        dp[0] = 0;
        for (int mask = 0; mask < N; mask++) {
            int killed = BitCount(mask);
            long gain = killed + 1;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                long need = (power[i] + gain - 1) / gain;
                int nm = mask | (1 << i);
                dp[nm] = Math.min(dp[nm], dp[mask] + need);
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
