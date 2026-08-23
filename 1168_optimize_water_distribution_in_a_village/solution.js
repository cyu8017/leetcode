// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

/**
 * @param {number} n
 * @param {number[]} wells
 * @param {number[][]} pipes
 * @return {number}
 */
var minCostToSupplyWater = function(n, wells, pipes) {
    const parent = Array.from({ length: n + 1 }, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const edges = wells.map((w, i) => [0, i + 1, w]).concat(pipes);
    edges.sort((a, b) => a[2] - b[2]);
    let ans = 0;
    for (const [a, b, cost] of edges) {
        const ra = find(a), rb = find(b);
        if (ra === rb) continue;
        parent[rb] = ra;
        ans += cost;
    }
    return ans;
};
