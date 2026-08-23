// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

using System.Collections.Generic;

public class Solution {
    public int NumberOfWays(int n, int x) {
        const int MOD = 1000000007;
        var powers = new List<int>();
        for (int i = 1; ; i++) {
            long p = 1;
            for (int j = 0; j < x; j++) {
                p *= i;
                if (p > n) break;
            }
            if (p > n) break;
            powers.Add((int)p);
        }
        int[] dp = new int[n + 1];
        dp[0] = 1;
        foreach (int p in powers) {
            for (int s = n; s >= p; s--)
                dp[s] = (dp[s] + dp[s - p]) % MOD;
        }
        return dp[n];
    }
}
