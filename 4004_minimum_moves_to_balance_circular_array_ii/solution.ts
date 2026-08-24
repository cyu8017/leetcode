// LeetCode 4004 - Minimum Moves to Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

export class MinCostMaxFlow {
    constructor(n_: any) {
    this.n = n_;
    this.graph = Array.from({length: n_}, () => []);
}
    addEdge(u: any, v: any, cap: any, cost: any): any {
    this.graph[u].push(new Edge(v, cap, cost, this.graph[v].length));
    this.graph[v].push(new Edge(u, 0, -cost, this.graph[u].length - 1));
}
    minCostFlow(source: any, sink: any, maxFlow: any): any {
    let totalCost = 0;
    let currentFlow = 0;
    const n = this.n;
    const graph = this.graph;
    while (currentFlow < maxFlow) {
        const dist = new Array(n).fill(INF);
        const parentNode = new Array(n).fill(-1);
        const parentEdge = new Array(n).fill(-1);
        const inQueue = new Array(n).fill(false);
        const q = [];
        q.push(source);
        dist[source] = 0;
        inQueue[source] = true;
        while (q.length > 0) {
            const u = q.shift();
            inQueue[u] = false;
            for (let i = 0; i < graph[u].length; i++) {
                const e = graph[u][i];
                if (e.cap > 0 && dist[e.to] > dist[u] + e.cost) {
                    dist[e.to] = dist[u] + e.cost;
                    parentNode[e.to] = u;
                    parentEdge[e.to] = i;
                    if (!inQueue[e.to]) {
                        inQueue[e.to] = true;
                        q.push(e.to);
                    }
                }
            }
        }
        if (dist[sink] === INF) return -1;
        let pushFlow = maxFlow - currentFlow;
        for (let cur = sink; cur !== source; cur = parentNode[cur]) {
            const e = graph[parentNode[cur]][parentEdge[cur]];
            if (e.cap < pushFlow) pushFlow = e.cap;
        }
        for (let cur = sink; cur !== source; cur = parentNode[cur]) {
            const p = parentNode[cur];
            const idx = parentEdge[cur];
            const rev = graph[p][idx].rev;
            graph[p][idx].cap -= pushFlow;
            graph[cur][rev].cap += pushFlow;
        }
        currentFlow += pushFlow;
        totalCost += pushFlow * dist[sink];
    }
    return totalCost;
}
}

const INF = 1000000000;

function Edge(to: any, cap: any, cost: any, rev: any): any {
    this.to = to; this.cap = cap; this.cost = cost; this.rev = rev;
}

export function minMoves(balance: any): any {
    let totalBalance = 0, totalDeficit = 0;
    for (const x of balance) {
        totalBalance += x;
        if (x < 0) totalDeficit += -x;
    }
    if (totalBalance < 0) return -1;
    if (totalDeficit === 0) return 0;
    const n = balance.length;
    const source = n, sink = n + 1;
    const mcmf = new MinCostMaxFlow(n + 2);
    for (let i = 0; i < n; i++) {
        const x = balance[i];
        if (x > 0) mcmf.addEdge(source, i, x, 0);
        else if (x < 0) mcmf.addEdge(i, sink, -x, 0);
        mcmf.addEdge(i, (i + 1) % n, INF, 1);
        mcmf.addEdge(i, (i - 1 + n) % n, INF, 1);
    }
    return mcmf.minCostFlow(source, sink, totalDeficit);
}
