// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

/**
 * @param {number[]} prices
 * @param {number[][]} queries
 * @return {number[]}
 */
var minimumRelativeLosses = function(prices, queries) {
    prices.sort((a, b) => a - b);
    const n = prices.length;
    const ans = Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const kk = queries[qi][0], m = queries[qi][1];
        const losses = Array(n);
        for (let i = 0; i < n; i++) {
            if (prices[i] <= kk) losses[i] = prices[i];
            else losses[i] = 2 * kk - prices[i];
        }
        losses.sort((a, b) => a - b);
        let sum = 0;
        for (let i = 0; i < m; i++) sum += losses[i];
        ans[qi] = sum;
    }
    return ans;
};
