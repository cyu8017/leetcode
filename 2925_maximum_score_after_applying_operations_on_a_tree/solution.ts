// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

export function maximumScoreAfterOperations(edges: number[][], values: number[]): number {
    const n = values.length;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    let total = 0;
    for (const v of values) total += v;
    const dfs = (u, p) => {
        let sumKids = 0;
        let isLeaf = true;
        for (const v of g[u]) {
            if (v === p) continue;
            isLeaf = false;
            sumKids += dfs(v, u);
        }
        if (isLeaf) return values[u];
        return values[u] < sumKids ? values[u] : sumKids;
    };
    return total - dfs(0, -1);
}
