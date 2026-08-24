// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

function buildTree(n: any, edges: any): any {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    return g;
}function countWithin(g: any, start: any, k: any): any {
    if (k < 0) return 0;
    const n = g.length;
    const vis = new Array(n).fill(false);
    const q = [[start, 0]];
    vis[start] = true;
    let cnt = 0;
    while (q.length) {
        const cur = q.shift();
        const u = cur[0], d = cur[1];
        cnt++;
        if (d === k) continue;
        for (const v of g[u]) {
            if (!vis[v]) {
                vis[v] = true;
                q.push([v, d + 1]);
            }
        }
    }
    return cnt;
}export function maxTargetNodes(edges1: any, edges2: any, k: any): any {
    const n = edges1.length + 1;
    const m = edges2.length + 1;
    const g1 = buildTree(n, edges1);
    const g2 = buildTree(m, edges2);
    const cnt1 = new Array(n);
    for (let i = 0; i < n; i++) cnt1[i] = countWithin(g1, i, k);
    let best2 = 0;
    if (k > 0) {
        for (let i = 0; i < m; i++) {
            const c = countWithin(g2, i, k - 1);
            if (c > best2) best2 = c;
        }
    }
    const ans = new Array(n);
    for (let i = 0; i < n; i++) ans[i] = cnt1[i] + best2;
    return ans;
}
