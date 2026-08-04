// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minimumCost = function(n, connections) {
    const parent = Array.from({ length: n + 1 }, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const union = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra === rb) return false;
        parent[rb] = ra;
        return true;
    };
    connections.sort((a, b) => a[2] - b[2]);
    let cost = 0, edges = 0;
    for (const [a, b, w] of connections) {
        if (union(a, b)) {
            cost += w;
            edges++;
            if (edges === n - 1) return cost;
        }
    }
    return -1;
};
