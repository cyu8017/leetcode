// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

var lastMarkedNodes = function(edges) {
    const n = edges.length + 1;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const bfs = (start) => {
        const dist = new Array(n).fill(-1);
        const q = [start];
        dist[start] = 0;
        let far = start;
        while (q.length) {
            const u = q.shift();
            if (dist[u] > dist[far]) far = u;
            for (const v of g[u]) {
                if (dist[v] === -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return [far, dist];
    };
    const u = bfs(0)[0];
    const ru = bfs(u);
    const v = ru[0];
    const du = ru[1];
    const dv = bfs(v)[1];
    const ans = new Array(n);
    for (let i = 0; i < n; i++) ans[i] = du[i] >= dv[i] ? u : v;
    return ans;
};
