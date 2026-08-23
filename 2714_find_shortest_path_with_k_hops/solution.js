// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

var shortestPathWithHops = function(n, edges, s, d, k) {
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    const dist = Array.from({ length: n }, () => new Array(k + 1).fill(Number.MAX_SAFE_INTEGER / 4));
    dist[s][0] = 0;
    const pq = [[s, 0, 0]];
    const push = (u, hops, cost) => {
        pq.push([u, hops, cost]);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[p][2] <= pq[i][2]) break;
            [pq[p], pq[i]] = [pq[i], pq[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = pq[0];
        const last = pq.pop();
        if (pq.length) {
            pq[0] = last;
            let i = 0;
            while (true) {
                let s2 = i, l = i * 2 + 1, r = l + 1;
                if (l < pq.length && pq[l][2] < pq[s2][2]) s2 = l;
                if (r < pq.length && pq[r][2] < pq[s2][2]) s2 = r;
                if (s2 === i) break;
                [pq[s2], pq[i]] = [pq[i], pq[s2]];
                i = s2;
            }
        }
        return top;
    };
    while (pq.length) {
        const [u, hops, cd] = pop();
        if (u === d) return cd;
        if (cd > dist[u][hops]) continue;
        for (const [to, w] of g[u]) {
            if (cd + w < dist[to][hops]) {
                dist[to][hops] = cd + w;
                push(to, hops, dist[to][hops]);
            }
            if (hops < k && cd < dist[to][hops + 1]) {
                dist[to][hops + 1] = cd;
                push(to, hops + 1, cd);
            }
        }
    }
    return -1;
};
