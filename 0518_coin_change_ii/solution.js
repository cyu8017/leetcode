// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

class Solution {
    change(amount, coins) {
        const dp = Array(amount + 1).fill(0);
        dp[0] = 1;
        for (const coin of coins) {
            for (let value = coin; value <= amount; value += 1) {
                dp[value] += dp[value - coin];
            }
        }
        return dp[amount];
    }
}

module.exports = { Solution };
