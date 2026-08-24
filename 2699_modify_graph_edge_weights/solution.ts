// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

export function modifiedGraphEdges(n: any, edges: any, source: any, destination: any, target: any): any {
    const INF = 2000000000;
    const dijkstra = (ignoreNeg) => {
        const dist = new Array(n).fill(INF);
        dist[source] = 0;
        const pq = [[source, 0]];
        const push = (u, d) => {
            pq.push([u, d]);
            let i = pq.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (pq[p][1] <= pq[i][1]) break;
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
                    let s = i, l = i * 2 + 1, r = l + 1;
                    if (l < pq.length && pq[l][1] < pq[s][1]) s = l;
                    if (r < pq.length && pq[r][1] < pq[s][1]) s = r;
                    if (s === i) break;
                    [pq[s], pq[i]] = [pq[i], pq[s]];
                    i = s;
                }
            }
            return top;
        };
        while (pq.length) {
            const [u, d] = pop();
            if (d !== dist[u]) continue;
            for (const e of edges) {
                let a = e[0], b = e[1], w = e[2];
                if (a !== u && b !== u) continue;
                const to = a === u ? b : a;
                if (w === -1) {
                    if (ignoreNeg) continue;
                    w = 1;
                }
                if (d + w < dist[to]) {
                    dist[to] = d + w;
                    push(to, dist[to]);
                }
            }
        }
        return dist;
    };
    let d = dijkstra(true);
    if (d[destination] < target) return [];
    let matched = d[destination] === target;
    for (let i = 0; i < edges.length; i++) {
        if (edges[i][2] !== -1) continue;
        if (matched) {
            edges[i][2] = INF;
            continue;
        }
        edges[i][2] = 1;
        d = dijkstra(false);
        if (d[destination] <= target) {
            edges[i][2] += target - d[destination];
            matched = true;
        }
    }
    d = dijkstra(false);
    if (d[destination] !== target) return [];
    return edges;
}
