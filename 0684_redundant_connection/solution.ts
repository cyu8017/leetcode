// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

export function findRedundantConnection(edges: number[][]): number[] {
    const find = (parent, x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const parent = Array.from({length: edges.length + 1}, (_, i) => i);
    for (const edge of edges) {
        const u = edge[0], v = edge[1];
        const pu = find(parent, u), pv = find(parent, v);
        if (pu === pv) return [u, v];
        parent[pu] = pv;
    }
    return [];
}
