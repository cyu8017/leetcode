// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

export function maxProfit(prices: number[]): number {
    if (prices.length === 0) {
        return 0;
    }
    let free = 0;
    let hold = -prices[0];
    let cooldown = 0;
    for (let index = 1; index < prices.length; index += 1) {
        const price = prices[index];
        [free, hold, cooldown] = [
            Math.max(free, cooldown),
            Math.max(hold, free - price),
            hold + price,
        ];
    }
    return Math.max(free, cooldown);
}
