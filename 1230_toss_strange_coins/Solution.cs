// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

public class Solution {
    public double ProbabilityOfHeads(int[] prob, int target) {
        var dp = new double[target + 1];
        dp[0] = 1.0;
        foreach (double p in prob) {
            for (int heads = target; heads >= 0; heads--) {
                dp[heads] = dp[heads] * (1 - p) + (heads > 0 ? dp[heads - 1] * p : 0);
            }
        }
        return dp[target];
    }
}
