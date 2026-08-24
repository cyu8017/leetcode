// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

export function findMaxPathScore(edges: any, online: any, k: any): any {
    const n = online.length;
    const g = Array.from({length: n}, () => []);
    let l = 2147483647, r = 0;
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        if (!online[u] || !online[v]) continue;
        g[u].push([v, w]);
        l = Math.min(l, w);
        r = Math.max(r, w);
    }
    if (l === 2147483647) return -1;
    const check = (mid) => {
        const INF = 1073741823;
        const dist = new Array(n).fill(INF);
        dist[0] = 0;
        const pq = [[0, 0]];
        const less = (a, b) => a[0] < b[0];
        while (pq.length) {
            pq.sort((a, b) => a[0] - b[0]);
            const cur = pq.shift();
            const d = cur[0], u = cur[1];
            if (d > k) return false;
            if (u === n - 1) return true;
            if (dist[u] < d) continue;
            for (const e of g[u]) {
                const v = e[0], w = e[1];
                if (w < mid) continue;
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push([nd, v]);
                }
            }
        }
        return false;
    };
    while (l < r) {
        const mid = (l + r + 1) >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return check(l) ? l : -1;
}
