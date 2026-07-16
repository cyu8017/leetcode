// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

export function maxProfit(prices: number[]): number {
    let minPrice = Infinity;
    let best = 0;

    for (const price of prices) {
        if (price < minPrice) {
            minPrice = price;
        } else {
            best = Math.max(best, price - minPrice);
        }
    }

    return best;
}