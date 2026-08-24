// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

var minimumCoins = function(prices) {
    const n = prices.length;
    const dp = new Array(n + 1).fill(1 << 30);
    dp[0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = i; j <= n && j <= 2 * i; j++) {
            dp[j] = Math.min(dp[j], dp[i - 1] + prices[i - 1]);
        }
    }
    return dp[n];
};
