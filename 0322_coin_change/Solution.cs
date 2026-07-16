// LeetCode 0322 - Coin Change

// https://leetcode.com/problems/coin-change/



public class Solution {

    public int CoinChange(int[] coins, int amount) {

        int maxValue = amount + 1;

        int[] dp = new int[amount + 1];

        for (int index = 1; index <= amount; index++) {

            dp[index] = maxValue;

        }

        dp[0] = 0;

        foreach (int coin in coins) {

            for (int value = coin; value <= amount; value++) {

                dp[value] = System.Math.Min(dp[value], dp[value - coin] + 1);

            }

        }

        return dp[amount] == maxValue ? -1 : dp[amount];

    }

}

