// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

export function maxScore(prices: number[]): number {
    const best = new Map();
    let ans = 0;
    for (let i = 0; i < prices.length; i++) {
        const key = prices[i] - (i + 1);
        const cand = (best.get(key) || 0) + prices[i];
        if (cand > (best.get(key) || 0)) best.set(key, cand);
        if (best.get(key) > ans) ans = best.get(key);
    }
    return ans;
}
