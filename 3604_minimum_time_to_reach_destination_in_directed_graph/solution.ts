// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

export function minTime(n: any, edges: any): any {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) g[e[0]].push([e[1], e[2], e[3]]);
    const Inf = 1e18;
    const dist = new Array(n).fill(Inf);
    dist[0] = 0;
    const pq = [[0, 0]];
    function push(t: any, u: any): any {
        let lo = 0, hi = pq.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (pq[mid][0] < t) lo = mid + 1;
            else hi = mid;
        }
        pq.splice(lo, 0, [t, u]);
    }    while (pq.length) {
        const cur = pq.shift();
        const t = cur[0], u = cur[1];
        if (t !== dist[u]) continue;
        if (u === n - 1) return t;
        for (const e of g[u]) {
            let nt = t;
            if (nt > e[2]) continue;
            if (nt < e[1]) nt = e[1];
            nt += 1;
            if (nt < dist[e[0]]) {
                dist[e[0]] = nt;
                push(nt, e[0]);
            }
        }
    }
    return dist[n - 1] === Inf ? -1 : dist[n - 1];
}
