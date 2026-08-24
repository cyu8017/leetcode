// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

/**
 * @param {number[][]} edges
 * @param {number} bob
 * @param {number[]} amount
 * @return {number}
 */
var mostProfitablePath = function(edges, bob, amount) {
    const n = amount.length;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const bobTime = Array(n).fill(n);
    const findBob = (u, p, t) => {
        if (u === 0) {
            bobTime[u] = t;
            return true;
        }
        for (const v of g[u]) {
            if (v === p) continue;
            if (findBob(v, u, t + 1)) {
                bobTime[u] = t;
                return true;
            }
        }
        return false;
    };
    findBob(bob, -1, 0);
    let ans = -Infinity;
    const dfs = (u, p, t, income) => {
        let cur = amount[u];
        if (t > bobTime[u]) cur = 0;
        else if (t === bobTime[u]) cur = Math.floor(cur / 2);
        income += cur;
        let isLeaf = true;
        for (const v of g[u]) {
            if (v !== p) {
                isLeaf = false;
                dfs(v, u, t + 1, income);
            }
        }
        if (isLeaf && income > ans) ans = income;
    };
    dfs(0, -1, 0, 0);
    return ans;
};
