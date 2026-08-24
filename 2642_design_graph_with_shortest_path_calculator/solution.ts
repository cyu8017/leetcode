// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

export class Graph {
    constructor(n: any, edges: any) {
    this.g = Array.from({ length: n }, () => []);
    for (const e of edges) this.g[e[0]].push([e[1], e[2]]);
}
    addEdge(edge: any): any {
    this.g[edge[0]].push([edge[1], edge[2]]);
}
    shortestPath(node1: any, node2: any): any {
    const n = this.g.length;
    const dist = new Array(n).fill(1 << 30);
    dist[node1] = 0;
    const pq = [[node1, 0]];
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
        if (u === node2) return d;
        if (d > dist[u]) continue;
        for (const [v, w] of this.g[u]) {
            const nd = d + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                push(v, nd);
            }
        }
    }
    return -1;
}
}
