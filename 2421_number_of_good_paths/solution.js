// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

/**
 * @param {number[]} vals
 * @param {number[][]} edges
 * @return {number}
 */
var numberOfGoodPaths = function(vals, edges) {
    const n = vals.length;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const parent = Array.from({ length: n }, (_, i) => i);
    const size = Array(n).fill(1);
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    const nodes = Array.from({ length: n }, (_, i) => i);
    nodes.sort((a, b) => vals[a] - vals[b]);
    let ans = n;
    for (let i = 0; i < n; ) {
        let j = i;
        while (j < n && vals[nodes[j]] === vals[nodes[i]]) j++;
        for (let k = i; k < j; k++) {
            const u = nodes[k];
            for (const v of g[u]) {
                if (vals[v] <= vals[u]) {
                    const ru = find(u), rv = find(v);
                    if (ru !== rv) {
                        parent[ru] = rv;
                        size[rv] += size[ru];
                    }
                }
            }
        }
        const freq = new Map();
        for (let k = i; k < j; k++) {
            const r = find(nodes[k]);
            freq.set(r, (freq.get(r) || 0) + 1);
        }
        for (const c of freq.values()) ans += (c * (c - 1)) / 2;
        i = j;
    }
    return ans;
};
