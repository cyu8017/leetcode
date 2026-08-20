"use strict";
// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
// @ts-nocheck
function findSmallestSetOfVertices(n, edges) {
    const incoming = new Set();
    for (const [, v] of edges)
        incoming.add(v);
    const ans = [];
    for (let v = 0; v < n; v++)
        if (!incoming.has(v))
            ans.push(v);
    return ans;
}
