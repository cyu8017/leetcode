// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

public class Solution {
    public int Change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        foreach (int coin in coins) {
            for (int value = coin; value <= amount; value++) {
                dp[value] += dp[value - coin];
            }
        }
        return dp[amount];
    }
}
