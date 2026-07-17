"use strict";
// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/
function getCoprimes(nums, edges) {
    const n = nums.length;
    const adj = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }
    const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b));
    const ans = new Array(n).fill(-1);
    const path = Array.from({ length: 51 }, () => []);
    const dfs = (node, parent, depth) => {
        let bestDepth = -1;
        let bestNode = -1;
        const val = nums[node];
        for (let d = 1; d <= 50; d++) {
            if (gcd(val, d) === 1 && path[d].length > 0) {
                const [candDepth, candNode] = path[d][path[d].length - 1];
                if (candDepth > bestDepth) {
                    bestDepth = candDepth;
                    bestNode = candNode;
                }
            }
        }
        ans[node] = bestNode;
        path[val].push([depth, node]);
        for (const nxt of adj[node]) {
            if (nxt !== parent) {
                dfs(nxt, node, depth + 1);
            }
        }
        path[val].pop();
    };
    dfs(0, -1, 0);
    return ans;
}
