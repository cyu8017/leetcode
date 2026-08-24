// LeetCode 2944 - Minimum Number of Coins for Fruits
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

var minimumCoins = function(prices) {
    const n = prices.length;
    const dp = new Array(n + 1).fill(1 << 30);
    dp[0] = 0;
    for (let i = 1; i <= n; i++)
        for (let j = i; j <= n && j <= i + i; j++) {
            const cand = dp[i - 1] + prices[i - 1];
            if (cand < dp[j]) dp[j] = cand;
        }
    return dp[n];
};
