// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

export function maxProfit(prices: number[], fee: number): number {
    let hold = -prices[0], cash = 0;
    for (let i = 1; i < prices.length; i++) {
        const price = prices[i];
        hold = Math.max(hold, cash - price);
        cash = Math.max(cash, hold + price - fee);
    }
    return cash;
}
