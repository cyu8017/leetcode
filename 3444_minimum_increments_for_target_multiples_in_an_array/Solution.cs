// LeetCode 3444 - Minimum Increments for Target Multiples in an Array
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/

public class Solution {
    static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
    static int Lcm(int a, int b) { return a / Gcd(a, b) * b; }

    public int MinimumIncrements(int[] nums, int[] target) {
        int m = target.Length;
        int N = 1 << m;
        const long inf = (long)1e18;
        long[] dp = new long[N];
        for (int i = 0; i < N; i++) dp[i] = inf;
        dp[0] = 0;
        foreach (int x in nums) {
            long[] ndp = (long[])dp.Clone();
            for (int mask = 0; mask < N; mask++) {
                for (int sub = 1; sub < N; sub++) {
                    int L = 1;
                    bool ok = true;
                    for (int i = 0; i < m; i++) {
                        if ((sub & (1 << i)) != 0) {
                            L = Lcm(L, target[i]);
                            if (L > 1000000000) { ok = false; break; }
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
        return (int)dp[N - 1];
    }
}
