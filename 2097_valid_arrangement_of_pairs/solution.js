// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

/**
 * @param {number[][]} pairs
 * @return {number[][]}
 */
var validArrangement = function(pairs) {
    const g = new Map();
    const indeg = new Map();
    const outdeg = new Map();
    for (const [u, v] of pairs) {
        if (!g.has(u)) g.set(u, []);
        g.get(u).push(v);
        outdeg.set(u, (outdeg.get(u) || 0) + 1);
        indeg.set(v, (indeg.get(v) || 0) + 1);
    }
    let start = pairs[0][0];
    for (const [u, o] of outdeg) {
        if (o - (indeg.get(u) || 0) === 1) { start = u; break; }
    }
    const path = [];
    const dfs = (u) => {
        const nbrs = g.get(u) || [];
        while (nbrs.length) {
            const v = nbrs.pop();
            dfs(v);
        }
        path.push(u);
    };
    dfs(start);
    path.reverse();
    const ans = [];
    for (let i = 0; i + 1 < path.length; i++) ans.push([path[i], path[i + 1]]);
    return ans;
};
