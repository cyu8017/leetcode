// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

export function maximumProfit(present: any, future: any, budget: any): any {
    const n = present.length;
    const dp = new Array(budget + 1).fill(0);
    for (let i = 0; i < n; i++) {
        const profit = future[i] - present[i];
        if (profit <= 0) continue;
        const cost = present[i];
        for (let b = budget; b >= cost; b--)
            dp[b] = Math.max(dp[b], dp[b - cost] + profit);
    }
    return dp[budget];
}
