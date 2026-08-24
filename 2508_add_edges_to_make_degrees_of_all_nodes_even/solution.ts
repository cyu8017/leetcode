// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

export function isPossible(n: number, edges: number[][]): boolean {
    const deg = Array(n + 1).fill(0);
    const adj = Array.from({ length: n + 1 }, () => new Set());
    for (const e of edges) {
        const u = e[0], v = e[1];
        deg[u]++;
        deg[v]++;
        adj[u].add(v);
        adj[v].add(u);
    }
    const odd = [];
    for (let i = 1; i <= n; i++) if (deg[i] % 2 === 1) odd.push(i);
    if (!odd.length) return true;
    if (odd.length === 2) {
        const a = odd[0], b = odd[1];
        if (!adj[a].has(b)) return true;
        for (let i = 1; i <= n; i++) {
            if (i !== a && i !== b && !adj[a].has(i) && !adj[b].has(i)) return true;
        }
        return false;
    }
    if (odd.length === 4) {
        const [a, b, c, d] = odd;
        return (!adj[a].has(b) && !adj[c].has(d)) ||
               (!adj[a].has(c) && !adj[b].has(d)) ||
               (!adj[a].has(d) && !adj[b].has(c));
    }
    return false;
}
