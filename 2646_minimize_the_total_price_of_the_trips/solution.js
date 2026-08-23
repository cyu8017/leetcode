// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

var minimumTotalPrice = function(n, edges, price, trips) {
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) { g[a].push(b); g[b].push(a); }
    const cnt = new Array(n).fill(0);
    const path = (u, p, target) => {
        if (u === target) { cnt[u]++; return true; }
        for (const v of g[u]) {
            if (v === p) continue;
            if (path(v, u, target)) { cnt[u]++; return true; }
        }
        return false;
    };
    for (const [a, b] of trips) path(a, -1, b);
    const dfs = (u, p) => {
        let full = price[u] * cnt[u], half = Math.floor(full / 2);
        for (const v of g[u]) {
            if (v === p) continue;
            const child = dfs(v, u);
            full += Math.min(child[0], child[1]);
            half += child[0];
        }
        return [full, half];
    };
    const res = dfs(0, -1);
    return Math.min(res[0], res[1]);
};
