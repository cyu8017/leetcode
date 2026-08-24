// LeetCode 2312 - Selling Pieces of Wood
// https://leetcode.com/problems/selling-pieces-of-wood/

export function sellingWood(m: number, n: number, prices: number[][]): number {
    const price = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    const dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
    for (const p of prices) price[p[0]][p[1]] = p[2];
    for (let h = 1; h <= m; ++h) {
        for (let w = 1; w <= n; ++w) {
            let best = price[h][w];
            for (let i = 1; i < h; ++i) best = Math.max(best, dp[i][w] + dp[h - i][w]);
            for (let j = 1; j < w; ++j) best = Math.max(best, dp[h][j] + dp[h][w - j]);
            dp[h][w] = best;
        }
    }
    return dp[m][n];
}
