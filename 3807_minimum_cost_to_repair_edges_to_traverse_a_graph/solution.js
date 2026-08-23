// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum_cost_to_repair_edges_to_traverse_a_graph/

var minCost = function(n, edges, k) {
    edges = edges.slice().sort((a, b) => a[2] - b[2]);
    const m = edges.length;
    if (m === 0) return -1;
    const check = (idx) => {
        const g = Array.from({length: n}, () => []);
        for (let i = 0; i <= idx; i++) {
            g[edges[i][0]].push(edges[i][1]);
            g[edges[i][1]].push(edges[i][0]);
        }
        let q = [0];
        const vis = new Array(n).fill(false);
        vis[0] = true;
        let dist = 0;
        while (q.length) {
            const nq = [];
            for (const u of q) {
                if (u === n - 1) return dist <= k;
                for (const v of g[u]) {
                    if (!vis[v]) {
                        vis[v] = true;
                        nq.push(v);
                    }
                }
            }
            q = nq;
            dist++;
        }
        return false;
    };
    let l = 0, r = m - 1;
    while (l < r) {
        const mid = (l + r) >> 1;
        if (check(mid)) r = mid;
        else l = mid + 1;
    }
    if (check(l)) return edges[l][2];
    return -1;
};
