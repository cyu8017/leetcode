// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} group
 * @param {number[][]} beforeItems
 * @return {number[]}
 */
var sortItems = function(n, m, group, beforeItems) {
    group = group.slice();
    for (let i = 0; i < n; i++) {
        if (group[i] === -1) group[i] = m++;
    }
    const itemGraph = Array.from({ length: n }, () => []);
    const itemIndeg = Array(n).fill(0);
    const groupGraph = Array.from({ length: m }, () => new Set());
    const groupIndeg = Array(m).fill(0);
    for (let v = 0; v < n; v++) {
        for (const u of beforeItems[v]) {
            itemGraph[u].push(v);
            itemIndeg[v]++;
            if (group[u] !== group[v] && !groupGraph[group[u]].has(group[v])) {
                groupGraph[group[u]].add(group[v]);
                groupIndeg[group[v]]++;
            }
        }
    }
    const topo = (graph, indeg) => {
        const q = [];
        for (let i = 0; i < indeg.length; i++) if (indeg[i] === 0) q.push(i);
        const order = [];
        let qi = 0;
        const adj = graph.map((g) => Array.isArray(g) ? g : [...g]);
        while (qi < q.length) {
            const u = q[qi++];
            order.push(u);
            for (const v of adj[u]) {
                indeg[v]--;
                if (indeg[v] === 0) q.push(v);
            }
        }
        return order.length === graph.length ? order : [];
    };
    const items = topo(itemGraph, itemIndeg);
    const groups = topo(groupGraph, groupIndeg.slice());
    if (!items.length || !groups.length) return [];
    const buckets = Array.from({ length: m }, () => []);
    for (const item of items) buckets[group[item]].push(item);
    const ans = [];
    for (const g of groups) ans.push(...buckets[g]);
    return ans;
};
