// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

export function maximalPathQuality(values: number[], edges: number[][], maxTime: number): number {
    const n = values.length;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    let ans = 0;
    const vis = new Array(n).fill(0);
    const dfs = (u, time, quality) => {
        if (time > maxTime) return;
        const first = vis[u] === 0;
        if (first) quality += values[u];
        vis[u]++;
        if (u === 0) ans = Math.max(ans, quality);
        for (const e of g[u]) dfs(e[0], time + e[1], quality);
        vis[u]--;
    };
    dfs(0, 0, 0);
    return ans;
}
