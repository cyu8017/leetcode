// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

/**
 * @param {number[][]} edges
 * @param {number[]} coins
 * @param {number} k
 * @return {number}
 */
var maximumPoints = function(edges, coins, k) {
    const n = coins.length;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const memo = new Map();
    const dfs = (u, p, shifts) => {
        if (shifts > 14) shifts = 14;
        const key = (u << 5) | shifts;
        if (memo.has(key)) return memo.get(key);
        const c = coins[u] >> shifts;
        let opt1 = c - k, opt2 = Math.floor(c / 2);
        for (const v of g[u]) {
            if (v === p) continue;
            opt1 += dfs(v, u, shifts);
            opt2 += dfs(v, u, shifts + 1);
        }
        const best = Math.max(opt1, opt2);
        memo.set(key, best);
        return best;
    };
    return dfs(0, -1, 0);
};
