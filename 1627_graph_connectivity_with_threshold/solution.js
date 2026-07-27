// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

/**
 * @param {number} n
 * @param {number} threshold
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var areConnected = function(n, threshold, queries) {
    const parent = Array.from({ length: n + 1 }, (_, i) => i);
    const find = (x) => {
        while (x !== parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    for (let d = threshold + 1; d <= n; d++) {
        for (let x = 2 * d; x <= n; x += d) {
            const a = find(d), b = find(x);
            if (a !== b) parent[b] = a;
        }
    }
    return queries.map(([a, b]) => find(a) === find(b));
};
