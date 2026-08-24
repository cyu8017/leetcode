// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

export function maxProfit(prices: number[], profits: number[]): number {
    const n = prices.length;
    let ans = -1;
    for (let j = 0; j < n; j++) {
        let bestL = -1, bestR = -1;
        for (let i = 0; i < j; i++)
            if (prices[i] < prices[j] && profits[i] > bestL) bestL = profits[i];
        for (let k = j + 1; k < n; k++)
            if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k];
        if (bestL >= 0 && bestR >= 0) {
            const cand = bestL + profits[j] + bestR;
            if (cand > ans) ans = cand;
        }
    }
    return ans;
}
