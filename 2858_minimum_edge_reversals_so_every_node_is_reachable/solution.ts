// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function minEdgeReversals(n: number, edges: number[][]): number[] {
    const g = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        g[u].push([v, 0]);
        g[v].push([u, 1]);
    }
    const ans = Array(n).fill(0);
    const dfs1 = (u, p) => {
        for (const [v, ww] of g[u]) {
            if (v === p) continue;
            ans[0] += ww;
            dfs1(v, u);
        }
    };
    const dfs2 = (u, p) => {
        for (const [v, ww] of g[u]) {
            if (v === p) continue;
            ans[v] = ww === 0 ? ans[u] + 1 : ans[u] - 1;
            dfs2(v, u);
        }
    };
    dfs1(0, -1);
    dfs2(0, -1);
    return ans;
}
