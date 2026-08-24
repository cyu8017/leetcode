// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

export function minTimeMaxPower(n: any, edges: any, power: any, cost: any, source: any, target: any): any {
    const INF = 2 ** 62;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) g[e[0]].push([e[1], e[2]]);
    const dist = Array.from({length: n}, () => new Array(power + 1).fill(INF));
    const pq = [[0, -power, source]];
    dist[source][power] = 0;
    while (pq.length) {
        pq.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
        const cur = pq.shift();
        let d = cur[0], p = -cur[1], u = cur[2];
        if (u === target) return [d, p];
        if (d > dist[u][p] || p < cost[u]) continue;
        p -= cost[u];
        for (const e of g[u]) {
            const v = e[0], t = e[1];
            const nd = d + t;
            if (nd < dist[v][p]) {
                dist[v][p] = nd;
                pq.push([nd, -p, v]);
            }
        }
    }
    return [-1, -1];
}
