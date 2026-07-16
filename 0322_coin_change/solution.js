// LeetCode 0322 - Coin Change
var coinChange = function(coins, amount) {
    const maxValue = amount + 1;
    const dp = Array(amount + 1).fill(maxValue);
    dp[0] = 0;
    for (const coin of coins) {
        for (let value = coin; value <= amount; value += 1) {
            dp[value] = Math.min(dp[value], dp[value - coin] + 1);
        }
    }
    return dp[amount] === maxValue ? -1 : dp[amount];
};
