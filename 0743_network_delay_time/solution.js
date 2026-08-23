// LeetCode 0743 - Network Delay Time
// https://leetcode.com/problems/network-delay-time/

/**
 * @param {number[][]} times
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var networkDelayTime = function(times, n, k) {
    const graph = Array.from({length: n + 1}, () => []);
    for (const edge of times) graph[edge[0]].push([edge[1], edge[2]]);
    const INF = Math.floor(Infinity / 4);
    const dist = new Array(n + 1).fill(INF);
    dist[k] = 0;
    const heap = [[0, k]];
    while (heap.length > 0) {
        heap.sort((a, b) => a[0] - b[0]);
        const [d, node] = heap.shift();
        if (d > dist[node]) continue;
        for (const e of graph[node]) {
            const nd = d + e[1];
            if (nd < dist[e[0]]) {
                dist[e[0]] = nd;
                heap.push([nd, e[0]]);
            }
        }
    }
    let ans = 0;
    for (let i = 1; i <= n; i++) ans = Math.max(ans, dist[i]);
    return ans === INF ? -1 : ans;
};
