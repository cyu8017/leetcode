// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

/**
 * @param {number[][]} edges
 * @param {number[]} patience
 * @return {number}
 */
var networkBecomesIdle = function(edges, patience) {
    const n = patience.length;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) { g[e[0]].push(e[1]); g[e[1]].push(e[0]); }
    const dist = new Array(n).fill(-1);
    const q = [0];
    dist[0] = 0;
    while (q.length) {
        const u = q.shift();
        for (const v of g[u]) if (dist[v] === -1) { dist[v] = dist[u] + 1; q.push(v); }
    }
    let ans = 0;
    for (let i = 1; i < n; i++) {
        const round = dist[i] * 2;
        const lastSend = Math.floor((round - 1) / patience[i]) * patience[i];
        ans = Math.max(ans, lastSend + round);
    }
    return ans + 1;
};
