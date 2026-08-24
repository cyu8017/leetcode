// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var distanceToCycle = function(n, edges) {
    const g = Array.from({length: n}, () => []);
    const deg = new Array(n).fill(0);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
        deg[e[0]]++;
        deg[e[1]]++;
    }
    const q = [];
    for (let i = 0; i < n; i++) if (deg[i] === 1) q.push(i);
    const onCycle = new Array(n).fill(true);
    while (q.length) {
        const u = q.shift();
        onCycle[u] = false;
        for (const v of g[u]) {
            if (--deg[v] === 1) q.push(v);
        }
    }
    const ans = new Array(n).fill(-1);
    const qq = [];
    for (let i = 0; i < n; i++) if (onCycle[i]) {
        ans[i] = 0;
        qq.push(i);
    }
    while (qq.length) {
        const u = qq.shift();
        for (const v of g[u]) if (ans[v] === -1) {
            ans[v] = ans[u] + 1;
            qq.push(v);
        }
    }
    return ans;
};
