// LeetCode 2603 - Collect Coins in a Tree
// https://leetcode.com/problems/collect-coins-in-a-tree/

/**
 * @param {number[]} coins
 * @param {number[][]} edges
 * @return {number}
 */
var collectTheCoins = function(coins, edges) {
    const n = coins.length;
    const g = Array.from({ length: n }, () => new Set());
    for (const e of edges) {
        g[e[0]].add(e[1]);
        g[e[1]].add(e[0]);
    }
    const deg = new Array(n);
    for (let i = 0; i < n; ++i) deg[i] = g[i].size;
    const q = [];
    for (let i = 0; i < n; ++i) {
        if (deg[i] === 1 && coins[i] === 0) q.push(i);
    }
    while (q.length) {
        const u = q.shift();
        for (const v of [...g[u]]) {
            g[v].delete(u);
            deg[v]--;
            if (deg[v] === 1 && coins[v] === 0) q.push(v);
        }
        g[u].clear();
        deg[u] = 0;
    }
    for (let round = 0; round < 2; ++round) {
        const leaves = [];
        for (let i = 0; i < n; ++i) if (deg[i] === 1) leaves.push(i);
        for (const u of leaves) {
            for (const v of [...g[u]]) {
                g[v].delete(u);
                deg[v]--;
            }
            g[u].clear();
            deg[u] = 0;
        }
    }
    let remain = 0;
    for (let i = 0; i < n; ++i) remain += g[i].size;
    return remain;
};
