// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

export function maxProfit(prices: number[], profits: number[]): number {
    const n = prices.length;
    let ans = -1;
    const bit = Array(5002).fill(0);
    const update = (i, val) => {
        for (; i < bit.length; i += i & -i)
            if (val > bit[i]) bit[i] = val;
    };
    const query = (i) => {
        let best = -1;
        for (; i > 0; i -= i & -i)
            if (bit[i] > best) best = bit[i];
        return best;
    };
    const maxLeft = Array(n);
    for (let j = 0; j < n; j++) {
        maxLeft[j] = query(prices[j] - 1);
        update(prices[j], profits[j]);
    }
    for (let j = 0; j < n; j++) {
        let bestR = -1;
        for (let k = j + 1; k < n; k++)
            if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k];
        if (maxLeft[j] >= 0 && bestR >= 0) {
            const cand = maxLeft[j] + profits[j] + bestR;
            if (cand > ans) ans = cand;
        }
    }
    return ans;
}
