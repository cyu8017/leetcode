// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

export function longestCycle(edges: number[]): number {
    const n = edges.length;
    const vis = Array(n).fill(false);
    let ans = -1;
    for (let i = 0; i < n; i++) {
        if (vis[i]) continue;
        const dist = new Map();
        let cur = i, step = 0;
        while (cur !== -1 && !vis[cur]) {
            vis[cur] = true;
            dist.set(cur, step);
            cur = edges[cur];
            step++;
        }
        if (cur !== -1 && dist.has(cur)) {
            ans = Math.max(ans, step - dist.get(cur));
        }
    }
    return ans;
}
