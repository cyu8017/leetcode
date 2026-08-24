// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

function buildTree(n: any, edges: any): any {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    return g;
}function bipartiteCount(g: any, color: any): any {
    color.fill(-1);
    const q = [0];
    color[0] = 0;
    const cnt = [1, 0];
    while (q.length) {
        const u = q.shift();
        for (const v of g[u]) {
            if (color[v] === -1) {
                color[v] = color[u] ^ 1;
                cnt[color[v]]++;
                q.push(v);
            }
        }
    }
    return cnt;
}export function maxTargetNodes(edges1: any, edges2: any): any {
    const n = edges1.length + 1;
    const m = edges2.length + 1;
    const g1 = buildTree(n, edges1);
    const g2 = buildTree(m, edges2);
    const color1 = new Array(n), color2 = new Array(m);
    const c1 = bipartiteCount(g1, color1);
    const c2 = bipartiteCount(g2, color2);
    const best2 = Math.max(c2[0], c2[1]);
    const ans = new Array(n);
    for (let i = 0; i < n; i++) ans[i] = c1[color1[i]] + best2;
    return ans;
}
