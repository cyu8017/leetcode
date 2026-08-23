// LeetCode 0322 - Coin Change

// https://leetcode.com/problems/coin-change/



class Solution {

    public int coinChange(int[] coins, int amount) {

        int maxValue = amount + 1;

        int[] dp = new int[amount + 1];

        for (int index = 1; index <= amount; index++) {

            dp[index] = maxValue;

        }

        dp[0] = 0;

        for (int coin : coins) {

            for (int value = coin; value <= amount; value++) {

                dp[value] = Math.min(dp[value], dp[value - coin] + 1);

            }

        }

        return dp[amount] == maxValue ? -1 : dp[amount];

    }

}

