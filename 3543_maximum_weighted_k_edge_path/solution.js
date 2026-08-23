// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

var maxWeight = function(n, edges, k, t) {
    const graph = Array.from({length: n}, () => []);
    for (const e of edges) graph[e[0]].push([e[1], e[2]]);
    const dp = Array.from({length: n}, () => Array.from({length: k + 1}, () => new Set()));
    for (let u = 0; u < n; u++) dp[u][0].add(0);
    for (let i = 0; i < k; i++) {
        for (let u = 0; u < n; u++) {
            for (const sum of dp[u][i]) {
                for (const e of graph[u]) {
                    const ns = sum + e[1];
                    if (ns < t) dp[e[0]][i + 1].add(ns);
                }
            }
        }
    }
    let ans = -1;
    for (let u = 0; u < n; u++)
        for (const sum of dp[u][k]) if (sum > ans) ans = sum;
    return ans;
};
