// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

var minCost = function(n, edges) {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        g[u].push([v, w]);
        g[v].push([u, w * 2]);
    }
    const inf = 1073741823;
    const dist = new Array(n).fill(inf);
    dist[0] = 0;
    const pq = [[0, 0]];
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const cur = pq.shift();
        const d = cur[0], u = cur[1];
        if (d > dist[u]) continue;
        if (u === n - 1) return d;
        for (const e of g[u]) {
            const v = e[0], w = e[1];
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                pq.push([nd, v]);
            }
        }
    }
    return -1;
};
