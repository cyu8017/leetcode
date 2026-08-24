// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

export function maximumProfit(prices: any, k: any): any {
    const n = prices.length;
    const f = Array.from({length: n}, () =>
        Array.from({length: k + 1}, () => [0, 0, 0]));
    for (let j = 1; j <= k; j++) {
        f[0][j][1] = -prices[0];
        f[0][j][2] = prices[0];
    }
    for (let i = 1; i < n; i++) {
        for (let j = 1; j <= k; j++) {
            f[i][j][0] = Math.max(f[i - 1][j][0], Math.max(f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]));
            f[i][j][1] = Math.max(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i]);
            f[i][j][2] = Math.max(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i]);
        }
    }
    return f[n - 1][k][0];
}
