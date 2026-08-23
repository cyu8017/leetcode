// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

var countCompleteComponents = function(n, edges) {
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) { g[a].push(b); g[b].push(a); }
    const vis = new Array(n).fill(false);
    let ans = 0;
    const dfs = (u, nodes) => {
        vis[u] = true;
        nodes.push(u);
        for (const v of g[u]) if (!vis[v]) dfs(v, nodes);
    };
    for (let i = 0; i < n; i++) {
        if (vis[i]) continue;
        const nodes = [];
        dfs(i, nodes);
        let ecount = 0;
        for (const u of nodes) ecount += g[u].length;
        ecount = Math.floor(ecount / 2);
        const sz = nodes.length;
        if (ecount === sz * (sz - 1) / 2) ans++;
    }
    return ans;
};
