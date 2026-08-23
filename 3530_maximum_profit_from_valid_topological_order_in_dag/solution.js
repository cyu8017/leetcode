// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

function pop(x) {
    let c = 0;
    while (x !== 0) { c += x & 1; x >>= 1; }
    return c;
}
var maxProfit = function(n, edges, score) {
    const need = new Array(n).fill(0);
    const dp = new Array(1 << n).fill(-1);
    dp[0] = 0;
    for (const e of edges) need[e[1]] |= 1 << e[0];
    for (let mask = 0; mask < (1 << n); mask++) {
        if (dp[mask] < 0) continue;
        const pos = pop(mask) + 1;
        for (let i = 0; i < n; i++) {
            if (((mask >> i) & 1) !== 0) continue;
            if ((mask & need[i]) === need[i]) {
                const nm = mask | (1 << i);
                const v = dp[mask] + score[i] * pos;
                if (v > dp[nm]) dp[nm] = v;
            }
        }
    }
    return dp[(1 << n) - 1];
};
