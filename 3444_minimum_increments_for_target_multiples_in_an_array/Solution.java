// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

import java.util.Arrays;

class Solution {
    private static int gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
    private static int lcm(int a, int b) { return a / gcd(a, b) * b; }

    public int minimumIncrements(int[] nums, int[] target) {
        int m = target.length;
        int N = 1 << m;
        final long inf = (long) 1e18;
        long[] dp = new long[N];
        Arrays.fill(dp, inf);
        dp[0] = 0;
        for (int x : nums) {
            long[] ndp = dp.clone();
            for (int mask = 0; mask < N; mask++) {
                for (int sub = 1; sub < N; sub++) {
                    int L = 1;
                    boolean ok = true;
                    for (int i = 0; i < m; i++) {
                        if ((sub & (1 << i)) != 0) {
                            L = lcm(L, target[i]);
                            if (L > 1_000_000_000) { ok = false; break; }
                        }
                    }
                    if (!ok) continue;
                    int cost = (L - x % L) % L;
                    int nmask = mask | sub;
                    if (dp[mask] + cost < ndp[nmask]) ndp[nmask] = dp[mask] + cost;
                }
            }
            dp = ndp;
        }
        return (int) dp[N - 1];
    }
}
