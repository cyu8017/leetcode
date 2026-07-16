// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount + 1];
        dp[0] = 1;
        for (int coin : coins) {
            for (int value = coin; value <= amount; value++) {
                dp[value] += dp[value - coin];
            }
        }
        return dp[amount];
    }
}
