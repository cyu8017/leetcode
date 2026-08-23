// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

/**
 * @param {number} k
 * @param {number[][]} rowConditions
 * @param {number[][]} colConditions
 * @return {number[][]}
 */
var buildMatrix = function(k, rowConditions, colConditions) {
    const topo = (conds) => {
        const g = Array.from({ length: k + 1 }, () => []);
        const indeg = Array(k + 1).fill(0);
        for (const c of conds) {
            g[c[0]].push(c[1]);
            indeg[c[1]]++;
        }
        const q = [];
        for (let i = 1; i <= k; i++) if (indeg[i] === 0) q.push(i);
        const order = [];
        while (q.length > 0) {
            const u = q.shift();
            order.push(u);
            for (const v of g[u]) {
                if (--indeg[v] === 0) q.push(v);
            }
        }
        if (order.length !== k) return null;
        return order;
    };
    const rowOrder = topo(rowConditions);
    const colOrder = topo(colConditions);
    if (!rowOrder || !colOrder) return [];
    const rowPos = Array(k + 1), colPos = Array(k + 1);
    for (let i = 0; i < k; i++) {
        rowPos[rowOrder[i]] = i;
        colPos[colOrder[i]] = i;
    }
    const ans = Array.from({ length: k }, () => Array(k).fill(0));
    for (let v = 1; v <= k; v++) ans[rowPos[v]][colPos[v]] = v;
    return ans;
};
