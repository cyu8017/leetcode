// LeetCode 3820 - Pythagorean Distance Nodes In A Tree
// https://leetcode.com/problems/pythagorean_distance_nodes_in_a_tree/

export function specialNodes(n: any, edges: any, x: any, y: any, z: any): any {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const bfs = (start) => {
        const dist = new Array(n).fill(1000000000);
        const q = [start];
        dist[start] = 0;
        for (let qi = 0; qi < q.length; qi++) {
            const u = q[qi];
            for (const v of g[u]) {
                if (dist[v] > dist[u] + 1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return dist;
    };
    const d1 = bfs(x), d2 = bfs(y), d3 = bfs(z);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const a = [d1[i], d2[i], d3[i]].sort((p, q) => p - q);
        const x0 = a[0], x1 = a[1], x2 = a[2];
        if (x0 * x0 + x1 * x1 === x2 * x2) ans++;
    }
    return ans;
}
