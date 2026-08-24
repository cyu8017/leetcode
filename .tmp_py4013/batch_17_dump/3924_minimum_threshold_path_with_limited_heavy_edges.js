// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

var minThreshold = function(n, edges, source, target, k) {
    if (source === target) return 0;
    const g = Array.from({length: n}, () => []);
    let maxWeight = 0;
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
        maxWeight = Math.max(maxWeight, e[2]);
    }
    if (!can(n, g, source, target, k, maxWeight)) return -1;
    let lo = 0, hi = maxWeight;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (can(n, g, source, target, k, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};

function can(n, g, source, target, k, threshold) {
    const inf = 1000000000;
    const dist = new Array(n).fill(inf);
    dist[source] = 0;
    const dq = [];
    dq.push(source);
    while (dq.length > 0) {
        const u = dq.shift();
        for (const e of g[u]) {
            const to = e[0], weight = e[1];
            const cost = weight > threshold ? 1 : 0;
            if (dist[u] + cost >= dist[to] || dist[u] + cost > k) continue;
            dist[to] = dist[u] + cost;
            if (cost === 0) dq.unshift(to);
            else dq.push(to);
        }
    }
    return dist[target] <= k;
}
