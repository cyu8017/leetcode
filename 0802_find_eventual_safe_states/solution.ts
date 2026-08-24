// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

export function eventualSafeNodes(graph: number[][]): number[] {
    const n = graph.length;
    const color = new Array(n).fill(0);
    const dfs = (node) => {
        if (color[node] !== 0) return color[node] === 2;
        color[node] = 1;
        for (const nei of graph[node]) {
            if (!dfs(nei)) return false;
        }
        color[node] = 2;
        return true;
    };
    const ans = [];
    for (let i = 0; i < n; i++) if (dfs(i)) ans.push(i);
    return ans;
}
