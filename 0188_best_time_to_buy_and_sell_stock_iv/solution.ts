// LeetCode 0188 - Best Time to Buy and Sell Stock IV
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

export function maxProfit(k: number, prices: number[]): number {
    const n = prices.length;
    if (n === 0 || k === 0) {
        return 0;
    }

    if (k >= Math.floor(n / 2)) {
        let profit = 0;
        for (let i = 1; i < n; i++) {
            profit += Math.max(prices[i] - prices[i - 1], 0);
        }
        return profit;
    }

    const buy = Array<number>(k + 1).fill(Infinity);
    const sell = Array<number>(k + 1).fill(0);
    for (const price of prices) {
        for (let transaction = 1; transaction <= k; transaction++) {
            buy[transaction] = Math.min(buy[transaction], price - sell[transaction - 1]);
            sell[transaction] = Math.max(sell[transaction], price - buy[transaction]);
        }
    }
    return sell[k];
}