"use strict";
// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
function countRestrictedPaths(n, edges) {
    const adj = Array.from({ length: n + 1 }, () => []);
    for (const [a, b, w] of edges) {
        adj[a].push([b, w]);
        adj[b].push([a, w]);
    }
    const dist = new Array(n + 1).fill(Infinity);
    dist[n] = 0;
    const heap = [[0, n]];
    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = (i - 1) >> 1;
            if (heap[parent][0] <= heap[i][0])
                break;
            [heap[parent], heap[i]] = [heap[i], heap[parent]];
            i = parent;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            for (;;) {
                let smallest = i;
                const l = 2 * i + 1;
                const r = 2 * i + 2;
                if (l < heap.length && heap[l][0] < heap[smallest][0])
                    smallest = l;
                if (r < heap.length && heap[r][0] < heap[smallest][0])
                    smallest = r;
                if (smallest === i)
                    break;
                [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return top;
    };
    while (heap.length > 0) {
        const [d, u] = pop();
        if (d !== dist[u])
            continue;
        for (const [v, w] of adj[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                push([nd, v]);
            }
        }
    }
    const order = [];
    for (let u = 1; u <= n; u++)
        order.push(u);
    order.sort((a, b) => dist[a] - dist[b]);
    const MOD = 1000000007;
    const cnt = new Array(n + 1).fill(0);
    cnt[n] = 1;
    for (const u of order) {
        if (u === n)
            continue;
        for (const [v] of adj[u]) {
            if (dist[u] > dist[v]) {
                cnt[u] = (cnt[u] + cnt[v]) % MOD;
            }
        }
    }
    return cnt[1];
}
