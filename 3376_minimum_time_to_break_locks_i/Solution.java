// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

import java.util.Arrays;
import java.util.List;

class Solution {
    private static int bitsOnes(int x) {
        int c = 0;
        while (x > 0) { c += x & 1; x >>= 1; }
        return c;
    }

    public int findMinimumTime(List<Integer> strength, int k) {
        int n = strength.size();
        final int inf = 1_000_000_000;
        int N = 1 << n;
        int[] dp = new int[N];
        Arrays.fill(dp, inf);
        dp[0] = 0;
        for (int mask = 0; mask < N; mask++) {
            if (dp[mask] == inf) continue;
            int opened = bitsOnes(mask);
            int x = 1 + opened * k;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) continue;
                int t = (strength.get(i) + x - 1) / x;
                int nmask = mask | (1 << i);
                if (dp[mask] + t < dp[nmask]) dp[nmask] = dp[mask] + t;
            }
        }
        return dp[N - 1];
    }
}
