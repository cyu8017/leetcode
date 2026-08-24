// LeetCode 3311 - Construct 2D Grid Matching Graph Layout
// https://leetcode.com/problems/construct-2d-grid-matching-graph-layout/

var constructGridLayout = function(n, edges) {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const deg = new Array(n);
    for (let i = 0; i < n; i++) deg[i] = g[i].length;
    let start = 0;
    for (let i = 0; i < n; i++) {
        if (deg[i] === 1) { start = i; break; }
        if (deg[i] === 2) start = i;
    }
    const vis = new Array(n).fill(false);
    const row = [];
    let cur = start, prev = -1;
    for (;;) {
        row.push(cur);
        vis[cur] = true;
        let next = -1;
        for (const v of g[cur]) {
            if (v !== prev && !vis[v] && deg[v] <= 3) {
                next = v;
                if (deg[v] < 4) break;
            }
        }
        if (next === -1) break;
        prev = cur;
        cur = next;
    }
    let width = row.length;
    let height = width !== 0 ? Math.floor(n / width) : n;
    if (width === 0 || width * height !== n) {
        for (let w = 1; w <= n; w++) {
            if (n % w === 0) { width = w; height = Math.floor(n / w); break; }
        }
    }
    const grid = Array.from({length: height}, () => new Array(width));
    for (let i = 0; i < n; i++) grid[Math.floor(i / width)][i % width] = i;
    return grid;
};
