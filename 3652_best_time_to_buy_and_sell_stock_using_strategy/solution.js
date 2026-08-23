// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

var maxProfit = function(prices, strategy, k) {
    const n = prices.length;
    const s = new Array(n + 1).fill(0);
    const t = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        s[i] = s[i - 1] + prices[i - 1] * strategy[i - 1];
        t[i] = t[i - 1] + prices[i - 1];
    }
    let ans = s[n];
    for (let i = k; i <= n; i++)
        ans = Math.max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - Math.floor(k / 2)]));
    return ans;
};
