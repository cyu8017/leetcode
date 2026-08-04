// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var countPaths = function(n, roads) {
    const MOD = 1000000007;
    const g = Array.from({ length: n }, () => []);
    for (const [u, v, t] of roads) {
        g[u].push([v, t]);
        g[v].push([u, t]);
    }
    const dist = new Array(n).fill(Infinity);
    const ways = new Array(n).fill(0);
    dist[0] = 0;
    ways[0] = 1;
    const pq = [[0, 0]];
    const push = (item) => {
        pq.push(item);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][0] <= pq[i][0]) break;
            [pq[p], pq[i]] = [pq[i], pq[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = pq[0];
        const last = pq.pop();
        if (!pq.length) return top;
        pq[0] = last;
        let i = 0;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < pq.length && pq[l][0] < pq[s][0]) s = l;
            if (r < pq.length && pq[r][0] < pq[s][0]) s = r;
            if (s === i) break;
            [pq[s], pq[i]] = [pq[i], pq[s]];
            i = s;
        }
        return top;
    };
    while (pq.length) {
        const [d, u] = pop();
        if (d > dist[u]) continue;
        for (const [v, w] of g[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                ways[v] = ways[u];
                push([nd, v]);
            } else if (nd === dist[v]) {
                ways[v] = (ways[v] + ways[u]) % MOD;
            }
        }
    }
    return ways[n - 1];
};
