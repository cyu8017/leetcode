// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/
// @ts-nocheck

function connectTwoGroups(cost: number[][]): number {
    const m = cost.length, n = cost[0].length;
    const full = 1 << n;
    const INF = 1e9;
    let dp = Array(full).fill(INF);
    dp[0] = 0;
    for (const row of cost) {
        const nxt = Array(full).fill(INF);
        for (let mask = 0; mask < full; mask++) {
            if (dp[mask] >= INF) continue;
            for (let j = 0; j < n; j++) {
                const newMask = mask | (1 << j);
                nxt[newMask] = Math.min(nxt[newMask], dp[mask] + row[j], nxt[mask] + row[j]);
            }
        }
        dp = nxt;
    }
    const minimum = Array.from({ length: n }, (_, j) => Math.min(...cost.map((row) => row[j])));
    let ans = INF;
    for (let mask = 0; mask < full; mask++) {
        let extra = 0;
        for (let j = 0; j < n; j++) {
            if (((mask >> j) & 1) === 0) extra += minimum[j];
        }
        ans = Math.min(ans, dp[mask] + extra);
    }
    return ans;
}
