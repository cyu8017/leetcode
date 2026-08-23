// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

using System;

public class Solution {
    public int ProfitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        const int MOD = 1_000_000_007;
        int[][] dp = new int[n + 1][];
        for (int i = 0; i <= n; i++) dp[i] = new int[minProfit + 1];
        dp[0][0] = 1;
        for (int i = 0; i < group.Length; i++) {
            int members = group[i], p = profit[i];
            for (int people = n; people >= members; people--) {
                for (int prof = minProfit; prof >= 0; prof--) {
                    int np = Math.Min(minProfit, prof + p);
                    dp[people][np] = (dp[people][np] + dp[people - members][prof]) % MOD;
                }
            }
        }
        int ans = 0;
        for (int people = 0; people <= n; people++)
            ans = (ans + dp[people][minProfit]) % MOD;
        return ans;
    }
}
