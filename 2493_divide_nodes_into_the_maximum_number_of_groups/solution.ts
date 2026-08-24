// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

export function magnificentSets(n: number, edges: number[][]): number {
    const g = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const bfsDepth = (start) => {
        const dist = Array(n + 1).fill(-1);
        const q = [start];
        dist[start] = 1;
        let best = 1;
        while (q.length) {
            const u = q.shift();
            if (dist[u] > best) best = dist[u];
            for (const v of g[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return best;
    };
    const color = Array(n + 1).fill(-1);
    const components = [];
    for (let i = 1; i <= n; i++) {
        if (color[i] !== -1) continue;
        const comp = [];
        const q = [i];
        color[i] = 0;
        let bipartite = true;
        while (q.length) {
            const u = q.shift();
            comp.push(u);
            for (const v of g[u]) {
                if (color[v] === -1) {
                    color[v] = color[u] ^ 1;
                    q.push(v);
                } else if (color[v] === color[u]) {
                    bipartite = false;
                }
            }
        }
        if (!bipartite) return -1;
        components.push(comp);
    }
    let ans = 0;
    for (const comp of components) {
        let best = 0;
        for (const u of comp) best = Math.max(best, bfsDepth(u));
        ans += best;
    }
    return ans;
}
