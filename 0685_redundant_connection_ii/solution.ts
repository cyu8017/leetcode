// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

export function findRedundantDirectedConnection(edges: number[][]): number[] {
    const find = (uf, x) => {
        while (uf[x] !== x) {
            uf[x] = uf[uf[x]];
            x = uf[x];
        }
        return x;
    };
    const n = edges.length;
    const parent = new Array(n + 1).fill(0);
    let cand1 = null, cand2 = null;
    for (let i = 0; i < n; i++) {
        const u = edges[i][0], v = edges[i][1];
        if (parent[v] === 0) parent[v] = u;
        else {
            cand1 = [parent[v], v];
            cand2 = [u, v];
            edges[i] = [-1, -1];
            break;
        }
    }
    const uf = Array.from({length: n + 1}, (_, i) => i);
    for (const edge of edges) {
        if (edge[0] < 0) continue;
        const pu = find(uf, edge[0]), pv = find(uf, edge[1]);
        if (pu === pv) return cand1 !== null ? cand1 : [edge[0], edge[1]];
        uf[pu] = pv;
    }
    return cand2;
}
