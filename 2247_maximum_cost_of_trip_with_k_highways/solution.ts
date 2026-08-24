// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

export function maximumCost(n: number, highways: number[][], k: number): number {
    if (k + 1 > n) return -1;
    const g = Array.from({length: n}, () => []);
    for (const h of highways) {
        g[h[0]].push([h[1], h[2]]);
        g[h[1]].push([h[0], h[2]]);
    }
    const dp = Array.from({length: 1 << n}, () => new Array(n).fill(-1));
    for (let i = 0; i < n; i++) dp[1 << i][i] = 0;
    let ans = -1;
    for (let mask = 0; mask < (1 << n); mask++) {
        const cities = mask.toString(2).split('1').length - 1;
        for (let u = 0; u < n; u++) {
            if (dp[mask][u] < 0) continue;
            if (cities - 1 === k) ans = Math.max(ans, dp[mask][u]);
            for (const [v, w] of g[u]) {
                if ((mask & (1 << v)) !== 0) continue;
                const nm = mask | (1 << v);
                dp[nm][v] = Math.max(dp[nm][v], dp[mask][u] + w);
            }
        }
    }
    return ans;
}
