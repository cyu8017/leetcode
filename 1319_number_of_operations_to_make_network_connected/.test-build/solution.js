"use strict";
// LeetCode 1319 - Number Of Operations To Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/
function makeConnected(n, connections) {
    if (connections.length < n - 1)
        return -1;
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        while (x !== parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    for (const [a, b] of connections) {
        const ra = find(a), rb = find(b);
        if (ra !== rb)
            parent[ra] = rb;
    }
    const roots = new Set();
    for (let i = 0; i < n; i++)
        roots.add(find(i));
    return roots.size - 1;
}
