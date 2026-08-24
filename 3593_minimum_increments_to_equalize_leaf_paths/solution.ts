// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

export function minIncrease(n: any, edges: any, cost: any): any {
    const graph = Array.from({length: n}, () => []);
    for (const e of edges) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }
    let ans = 0;
    function dfs(u: any, p: any): any {
        if (graph[u].length === 1 && p !== -1) return cost[u];
        const childVals = [];
        for (const v of graph[u]) {
            if (v === p) continue;
            childVals.push(dfs(v, u));
        }
        if (childVals.length === 0) return cost[u];
        let mx = 0;
        for (const c of childVals) mx = Math.max(mx, c);
        for (const c of childVals) if (c < mx) ans++;
        return mx + cost[u];
    }    dfs(0, -1);
    return ans;
}
