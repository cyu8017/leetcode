// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[][]}
 */
var getAncestors = function(n, edges) {
    const g = Array.from({length: n}, () => []);
    const indeg = new Array(n).fill(0);
    for (const [a, b] of edges) { g[a].push(b); indeg[b]++; }
    const anc = Array.from({length: n}, () => new Set());
    const q = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) q.push(i);
    while (q.length) {
        const u = q.shift();
        for (const v of g[u]) {
            anc[v].add(u);
            for (const x of anc[u]) anc[v].add(x);
            if (--indeg[v] === 0) q.push(v);
        }
    }
    return anc.map(s => [...s].sort((a, b) => a - b));
};
