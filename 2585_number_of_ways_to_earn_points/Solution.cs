// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

public class Solution {
    public int WaysToReachTarget(int target, int[][] types) {
        const int MOD = 1000000007;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        foreach (var t in types) {
            int count = t[0], marks = t[1];
            for (int s = target; s >= 0; --s) {
                for (int k = 1; k <= count && s - k * marks >= 0; ++k) {
                    dp[s] = (dp[s] + dp[s - k * marks]) % MOD;
                }
            }
        }
        return dp[target];
    }
}
