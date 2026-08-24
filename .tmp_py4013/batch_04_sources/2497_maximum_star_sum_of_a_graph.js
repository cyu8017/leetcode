// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

/**
 * @param {number[]} vals
 * @param {number[][]} edges
 * @param {number} k
 * @return {number}
 */
var maxStarSum = function(vals, edges, k) {
    const n = vals.length;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    let ans = vals[0];
    for (let i = 0; i < n; i++) {
        const neigh = [];
        for (const v of g[i]) {
            if (vals[v] > 0) neigh.push(vals[v]);
        }
        neigh.sort((a, b) => b - a);
        let sum = vals[i];
        for (let j = 0; j < neigh.length && j < k; j++) sum += neigh[j];
        if (sum > ans) ans = sum;
    }
    return ans;
};
